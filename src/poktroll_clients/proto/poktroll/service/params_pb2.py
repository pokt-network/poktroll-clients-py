# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: poktroll/service/params.proto
# Protobuf Python Version: 5.28.3
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
    3,
    '',
    'poktroll/service/params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from poktroll_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from poktroll_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from poktroll_clients.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dpoktroll/service/params.proto\x12\x10poktroll.service\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x9e\x01\n\x06Params\x12p\n\x0f\x61\x64\x64_service_fee\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB-\xea\xde\x1f\x0f\x61\x64\x64_service_fee\xf2\xde\x1f\x16yaml:\"add_service_fee\"R\raddServiceFee:\"\xe8\xa0\x1f\x01\x8a\xe7\xb0*\x19poktroll/x/service/ParamsB6Z0github.com/pokt-network/poktroll/x/service/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'poktroll.service.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z0github.com/pokt-network/poktroll/x/service/types\330\342\036\001'
  _globals['_PARAMS'].fields_by_name['add_service_fee']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['add_service_fee']._serialized_options = b'\352\336\037\017add_service_fee\362\336\037\026yaml:\"add_service_fee\"'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\350\240\037\001\212\347\260*\031poktroll/x/service/Params'
  _globals['_PARAMS']._serialized_start=125
  _globals['_PARAMS']._serialized_end=283
# @@protoc_insertion_point(module_scope)
