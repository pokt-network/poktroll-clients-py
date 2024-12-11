# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: poktroll/service/tx.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'poktroll/service/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from poktroll_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from poktroll_clients.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from poktroll_clients.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from poktroll_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from poktroll_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from poktroll_clients.proto.poktroll.service import params_pb2 as poktroll_dot_service_dot_params__pb2
from poktroll_clients.proto.poktroll.shared import service_pb2 as poktroll_dot_shared_dot_service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19poktroll/service/tx.proto\x12\x10poktroll.service\x1a\x11\x61mino/amino.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1dpoktroll/service/params.proto\x1a\x1dpoktroll/shared/service.proto\"\xbd\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12;\n\x06params\x18\x02 \x01(\x0b\x32\x18.poktroll.service.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params:5\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\"poktroll/x/service/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\xba\x01\n\x0eMsgUpdateParam\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x41\n\x07\x61s_coin\x18\t \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x0b\xea\xde\x1f\x07\x61s_coinH\x00R\x06\x61sCoin:\x0e\x82\xe7\xb0*\tauthorityB\t\n\x07\x61s_type\"J\n\x16MsgUpdateParamResponse\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32\x18.poktroll.service.ParamsR\x06params\"\x9c\x01\n\rMsgAddService\x12=\n\rowner_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0cownerAddress\x12\x38\n\x07service\x18\x02 \x01(\x0b\x32\x18.poktroll.shared.ServiceB\x04\xc8\xde\x1f\x00R\x07service:\x12\x82\xe7\xb0*\rowner_address\"\x17\n\x15MsgAddServiceResponse2\x9d\x02\n\x03Msg\x12\\\n\x0cUpdateParams\x12!.poktroll.service.MsgUpdateParams\x1a).poktroll.service.MsgUpdateParamsResponse\x12Y\n\x0bUpdateParam\x12 .poktroll.service.MsgUpdateParam\x1a(.poktroll.service.MsgUpdateParamResponse\x12V\n\nAddService\x12\x1f.poktroll.service.MsgAddService\x1a\'.poktroll.service.MsgAddServiceResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x36Z0github.com/pokt-network/poktroll/x/service/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'poktroll.service.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z0github.com/pokt-network/poktroll/x/service/types\330\342\036\001'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\"poktroll/x/service/MsgUpdateParams'
  _globals['_MSGUPDATEPARAM'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAM'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAM'].fields_by_name['as_coin']._loaded_options = None
  _globals['_MSGUPDATEPARAM'].fields_by_name['as_coin']._serialized_options = b'\352\336\037\007as_coin'
  _globals['_MSGUPDATEPARAM']._loaded_options = None
  _globals['_MSGUPDATEPARAM']._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGADDSERVICE'].fields_by_name['owner_address']._loaded_options = None
  _globals['_MSGADDSERVICE'].fields_by_name['owner_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGADDSERVICE'].fields_by_name['service']._loaded_options = None
  _globals['_MSGADDSERVICE'].fields_by_name['service']._serialized_options = b'\310\336\037\000'
  _globals['_MSGADDSERVICE']._loaded_options = None
  _globals['_MSGADDSERVICE']._serialized_options = b'\202\347\260*\rowner_address'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._serialized_start=235
  _globals['_MSGUPDATEPARAMS']._serialized_end=424
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=426
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=451
  _globals['_MSGUPDATEPARAM']._serialized_start=454
  _globals['_MSGUPDATEPARAM']._serialized_end=640
  _globals['_MSGUPDATEPARAMRESPONSE']._serialized_start=642
  _globals['_MSGUPDATEPARAMRESPONSE']._serialized_end=716
  _globals['_MSGADDSERVICE']._serialized_start=719
  _globals['_MSGADDSERVICE']._serialized_end=875
  _globals['_MSGADDSERVICERESPONSE']._serialized_start=877
  _globals['_MSGADDSERVICERESPONSE']._serialized_end=900
  _globals['_MSG']._serialized_start=903
  _globals['_MSG']._serialized_end=1188
# @@protoc_insertion_point(module_scope)
