# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pocket/shared/tx.proto
# Protobuf Python Version: 6.30.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    1,
    '',
    'pocket/shared/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pocket_clients.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pocket_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pocket_clients.proto.pocket.shared import params_pb2 as pocket_dot_shared_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16pocket/shared/tx.proto\x12\rpocket.shared\x1a\x11\x61mino/amino.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1apocket/shared/params.proto\"\xb7\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x38\n\x06params\x18\x02 \x01(\x0b\x32\x15.pocket.shared.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params:2\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1fpocket/x/shared/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\xfe\x01\n\x0eMsgUpdateParam\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12,\n\tas_string\x18\x03 \x01(\tB\r\xea\xde\x1f\tas_stringH\x00R\x08\x61sString\x12,\n\tas_uint64\x18\x06 \x01(\x04\x42\r\xea\xde\x1f\tas_uint64H\x00R\x08\x61sUint64\x12)\n\x08\x61s_bytes\x18\x07 \x01(\x0c\x42\x0c\xea\xde\x1f\x08\x61s_bytesH\x00R\x07\x61sBytes:\x0e\x82\xe7\xb0*\tauthorityB\t\n\x07\x61s_type\"G\n\x16MsgUpdateParamResponse\x12-\n\x06params\x18\x01 \x01(\x0b\x32\x15.pocket.shared.ParamsR\x06params2\xb9\x01\n\x03Msg\x12V\n\x0cUpdateParams\x12\x1e.pocket.shared.MsgUpdateParams\x1a&.pocket.shared.MsgUpdateParamsResponse\x12S\n\x0bUpdateParam\x12\x1d.pocket.shared.MsgUpdateParam\x1a%.pocket.shared.MsgUpdateParamResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x35Z/github.com/pokt-network/poktroll/x/shared/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pocket.shared.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z/github.com/pokt-network/poktroll/x/shared/types\330\342\036\001'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\037pocket/x/shared/MsgUpdateParams'
  _globals['_MSGUPDATEPARAM'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAM'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAM'].fields_by_name['as_string']._loaded_options = None
  _globals['_MSGUPDATEPARAM'].fields_by_name['as_string']._serialized_options = b'\352\336\037\tas_string'
  _globals['_MSGUPDATEPARAM'].fields_by_name['as_uint64']._loaded_options = None
  _globals['_MSGUPDATEPARAM'].fields_by_name['as_uint64']._serialized_options = b'\352\336\037\tas_uint64'
  _globals['_MSGUPDATEPARAM'].fields_by_name['as_bytes']._loaded_options = None
  _globals['_MSGUPDATEPARAM'].fields_by_name['as_bytes']._serialized_options = b'\352\336\037\010as_bytes'
  _globals['_MSGUPDATEPARAM']._loaded_options = None
  _globals['_MSGUPDATEPARAM']._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._serialized_start=163
  _globals['_MSGUPDATEPARAMS']._serialized_end=346
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=348
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=373
  _globals['_MSGUPDATEPARAM']._serialized_start=376
  _globals['_MSGUPDATEPARAM']._serialized_end=630
  _globals['_MSGUPDATEPARAMRESPONSE']._serialized_start=632
  _globals['_MSGUPDATEPARAMRESPONSE']._serialized_end=703
  _globals['_MSG']._serialized_start=706
  _globals['_MSG']._serialized_end=891
# @@protoc_insertion_point(module_scope)
