# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: poktroll/application/params.proto
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
    'poktroll/application/params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from poktroll_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from poktroll_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from poktroll_clients.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!poktroll/application/params.proto\x12\x14poktroll.application\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xfe\x01\n\x06Params\x12q\n\x16max_delegated_gateways\x18\x01 \x01(\x04\x42;\xea\xde\x1f\x16max_delegated_gateways\xf2\xde\x1f\x1dyaml:\"max_delegated_gateways\"R\x14maxDelegatedGateways\x12Y\n\tmin_stake\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB!\xea\xde\x1f\tmin_stake\xf2\xde\x1f\x10yaml:\"min_stake\"R\x08minStake:&\xe8\xa0\x1f\x01\x8a\xe7\xb0*\x1dpoktroll/x/application/ParamsB:Z4github.com/pokt-network/poktroll/x/application/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'poktroll.application.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/pokt-network/poktroll/x/application/types\330\342\036\001'
  _globals['_PARAMS'].fields_by_name['max_delegated_gateways']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['max_delegated_gateways']._serialized_options = b'\352\336\037\026max_delegated_gateways\362\336\037\035yaml:\"max_delegated_gateways\"'
  _globals['_PARAMS'].fields_by_name['min_stake']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['min_stake']._serialized_options = b'\352\336\037\tmin_stake\362\336\037\020yaml:\"min_stake\"'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\350\240\037\001\212\347\260*\035poktroll/x/application/Params'
  _globals['_PARAMS']._serialized_start=133
  _globals['_PARAMS']._serialized_end=387
# @@protoc_insertion_point(module_scope)
