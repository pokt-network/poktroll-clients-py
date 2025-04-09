from typing import List

from google.protobuf.message import Message
from nacl.signing import SigningKey

from pocket_clients import ffi, check_err, libpocket_clients
from pocket_clients.proto.pocket.shared.service_pb2 import SupplierServiceConfig
from pocket_clients.protobuf import SerializedProto, deserialize_protobuf, ProtoMessageArray


def new_signed_msg_claim_morse_account(shannon_dest_address: str,
                                       morse_priv_key_ref: ffi.CData) -> (Message, List[ffi.CData]):
    c_objects = []
    err_ptr = ffi.new("char **")
    c_objects.append(err_ptr)

    c_serialized_msg = libpocket_clients.NewSerializedSignedMsgClaimMorseAccount(
        shannon_dest_address.encode('utf-8'),
        morse_priv_key_ref,
        err_ptr)
    check_err(err_ptr)
    c_objects.append(c_serialized_msg)

    serialized_msg = SerializedProto.from_c_struct(c_serialized_msg)
    return deserialize_protobuf(serialized_msg), c_objects


def new_signed_msg_claim_morse_application(shannon_dest_address: str,
                                           morse_priv_key_ref: ffi.CData,
                                           service_id: str) -> (Message, List[ffi.CData]):
    c_objects = []
    err_ptr = ffi.new("char **")
    c_objects.append(err_ptr)

    c_serialized_msg = libpocket_clients.NewSerializedSignedMsgClaimMorseApplication(
        shannon_dest_address.encode('utf-8'),
        morse_priv_key_ref,
        ffi.new("char[]", service_id.encode('utf-8')),
        err_ptr)
    check_err(err_ptr)
    c_objects.append(c_serialized_msg)

    serialized_msg = SerializedProto.from_c_struct(c_serialized_msg)
    return deserialize_protobuf(serialized_msg), c_objects


def new_signed_msg_claim_morse_supplier(shannon_owner_address: str,
                                        shannon_operator_address: str,
                                        morse_priv_key_ref: ffi.CData,
                                        supplier_service_configs: List[SupplierServiceConfig]) -> (
        Message, List[ffi.CData]):
    c_objects = []
    err_ptr = ffi.new("char **")
    c_objects.append(err_ptr)

    c_supplier_service_configs = ProtoMessageArray(messages=[
        SerializedProto.from_proto(cfg) for cfg in supplier_service_configs
    ]).to_c_struct()
    c_objects.append(c_supplier_service_configs)

    c_serialized_msg = libpocket_clients.NewSerializedSignedMsgClaimMorseSupplier(
        shannon_owner_address.encode('utf-8'),
        shannon_operator_address.encode('utf-8'),
        morse_priv_key_ref,
        c_supplier_service_configs,
        err_ptr)
    check_err(err_ptr)
    c_objects.append(c_serialized_msg)

    serialized_msg = SerializedProto.from_c_struct(c_serialized_msg)
    return deserialize_protobuf(serialized_msg), c_objects
