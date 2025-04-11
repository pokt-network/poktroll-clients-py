import importlib
from dataclasses import dataclass
from pprint import pprint
from typing import List

from google.protobuf import symbol_database, message
from google.protobuf.message import Message

from pocket_clients import go_ref, libpocket_clients, check_err
from pocket_clients.cases import camel_to_snake_case
from pocket_clients.ffi import ffi


class SerializedProto:
    def __init__(self, type_url="", data=b""):
        self.type_url = type_url
        self.data = data

    def to_c_struct(self):
        c_struct = ffi.new("serialized_proto *")

        # Convert and store type_url
        self._type_url_bytes = self.type_url.encode('utf-8')
        self._c_type_url = ffi.new(f"uint8_t[{len(self._type_url_bytes)}]", self._type_url_bytes)
        c_struct.type_url = self._c_type_url
        c_struct.type_url_length = len(self._type_url_bytes)

        # Convert and store data
        self._c_data = ffi.new(f"uint8_t[{len(self.data)}]", self.data)
        c_struct.data = self._c_data
        c_struct.data_length = len(self.data)

        return c_struct

    @staticmethod
    def from_c_struct(c_serialized_proto: ffi.CData):
        return SerializedProto(
            type_url=(ffi.string(c_serialized_proto.type_url, c_serialized_proto.type_url_length).decode('utf-8')),
            data=(bytes(ffi.buffer(c_serialized_proto.data, c_serialized_proto.data_length))),
        )

    @staticmethod
    def from_proto(proto):
        return SerializedProto(
            type_url=proto.DESCRIPTOR.full_name,
            data=proto.SerializeToString()
        )


class SerializedProtoArray:
    def __init__(self, protos=None):
        self.protos = protos or []

    def to_c_struct(self):
        # Keep all C objects alive for the lifetime of this object
        self._all_c_objects = []

        # Create array structure
        c_array = ffi.new("serialized_proto_array *")
        c_array.num_protos = len(self.protos)

        # Create serialized_proto array
        c_messages = ffi.new(f"serialized_proto[{len(self.protos)}]")
        c_array.protos = c_messages

        # Store references to prevent GC
        self._all_c_objects.append(c_array)
        self._all_c_objects.append(c_messages)

        # Create and fill each message
        for i, msg in enumerate(self.protos):
            # Create type_url buffer
            type_url_bytes = msg.type_url.encode('utf-8')
            c_type_url = ffi.new(f"uint8_t[{len(type_url_bytes)}]", type_url_bytes)

            # Create data buffer
            c_data = ffi.new(f"uint8_t[{len(msg.data)}]", msg.data)

            # Set message fields
            c_messages[i].type_url = c_type_url
            c_messages[i].type_url_length = len(type_url_bytes)
            c_messages[i].data = c_data
            c_messages[i].data_length = len(msg.data)

            # Store references
            self._all_c_objects.append(c_type_url)
            self._all_c_objects.append(c_data)

        return c_array

    def to_messages(self) -> List[Message]:
        return [deserialize_protobuf(serialized_proto) for serialized_proto in self.protos]

    @staticmethod
    def from_c_struct(c_serialized_proto_array: ffi.CData):
        serialized_proto_array = SerializedProtoArray(protos=[])
        for i in range(c_serialized_proto_array.num_protos):
            serialized_proto = SerializedProto.from_c_struct(c_serialized_proto_array.protos[i])
            serialized_proto_array.protos.append(serialized_proto)

        return serialized_proto_array


def get_serialized_proto(go_proto_ref: go_ref) -> SerializedProto:
    """
    Converts a Go reference, which is assumed to be a concrete protobuf type, into
    the corresponding SerializedProto object. If the reference is not found or to
    a non-protobuf type, an error is raised.

    Args:
        go_proto_ref: Go reference to a protobuf message
    Returns:
        SerializedProto: SerializedProto object containing the type URL and data
        of the protobuf message
    Raises:
        FFIError: If the Go reference is not found or to a non-protobuf type
    """
    err_ptr = ffi.new("char **")

    c_serialized_proto = libpocket_clients.GetGoProtoAsSerializedProto(go_proto_ref, err_ptr)

    check_err(err_ptr)

    # TODO_IN_THIS_COMMIT: Free the C struct
    # NB: Caller is responsible for freeing the returned C struct.
    serialized_proto = SerializedProto.from_c_struct(c_serialized_proto)
    # ffi.free(c_serialized_proto)

    return serialized_proto


def deserialize_protobuf(serialized_proto: SerializedProto) -> message.Message:
    """
    Deserialize protocol buffer data given a type URL.

    Args:
        serialized_proto: SerializedProto object containing the serialized protobuf message.
    Returns:
        Deserialized protobuf message as its concrete type.
    Raises:
        ValueError: If type URL is invalid or message type cannot be found
        ImportError: If the protobuf module cannot be imported
    """

    # First, import the module containing the protobuf classes
    # This ensures the types are registered in the symbol database
    type_url = serialized_proto.type_url.lstrip("/")
    pocket_namespace = type_url.rsplit(".", 1)[0]
    filename_prefix = camel_to_snake_case(type_url.rsplit('.', 1)[1])
    package_filename = f"{filename_prefix}_pb2"
    package_module = f"pocket_clients.proto.{pocket_namespace}.{package_filename}"

    try:
        importlib.import_module(package_module)
    except ImportError as e:
        try:
            # NB: Fallback to importing the types_pb2 module if the main module fails
            package_module = f"pocket_clients.proto.{pocket_namespace}.types_pb2"
            importlib.import_module(package_module)
        except ImportError as e:
            raise ImportError(f"Could not import protobuf module {package_module}: {str(e)}")

    # Extract the full message type from the type URL
    if '/' in type_url:
        _, full_type = type_url.split('/', 1)
    else:
        full_type = type_url

    # Split into package and message type to validate format
    parts = full_type.split('.')
    if len(parts) < 2:
        raise ValueError("Invalid type URL format")

    try:
        # Get the message class from the symbol database
        db = symbol_database.Default()
        message_class = db.GetSymbol(full_type)

        # Create a new message instance and parse the data
        message = message_class()
        message.ParseFromString(serialized_proto.data)

        return message
        # # Convert to dictionary for easier handling
        # return MessageToDict(message)

    except KeyError as e:
        raise ValueError(
            f"Could not find message type: {full_type}. Make sure it's registered in the symbol database.") from e
    except Exception as e:
        raise ValueError(f"Error deserializing protobuf: {str(e)}") from e


def get_proto_from_go_ref(go_proto_ref: go_ref) -> message.Message:
    """
    Converts a Go reference, which is assumed to be a concrete protobuf type, into
    the corresponding Python protobuf message. If the reference is not found or to
    a non-protobuf type, an error is raised.

    Args:
        go_proto_ref: Go reference to a protobuf message
    Returns:
        message.Message: Deserialized protobuf message
    Raises:
        FFIError: If the Go reference is not found or to a non-protobuf type
        ValueError: If the type URL is invalid or the message type cannot be found
        ImportError: If the protobuf module cannot be imported
    """
    serialized_proto = get_serialized_proto(go_proto_ref)
    return deserialize_protobuf(serialized_proto)
