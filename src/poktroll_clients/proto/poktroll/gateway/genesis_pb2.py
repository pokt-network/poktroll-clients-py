# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: poktroll/gateway/genesis.proto
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
    'poktroll/gateway/genesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from poktroll_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from poktroll_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from poktroll_clients.proto.poktroll.gateway import params_pb2 as poktroll_dot_gateway_dot_params__pb2
from poktroll_clients.proto.poktroll.gateway import types_pb2 as poktroll_dot_gateway_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epoktroll/gateway/genesis.proto\x12\x10poktroll.gateway\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1dpoktroll/gateway/params.proto\x1a\x1cpoktroll/gateway/types.proto\"\x8f\x01\n\x0cGenesisState\x12;\n\x06params\x18\x01 \x01(\x0b\x32\x18.poktroll.gateway.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params\x12\x42\n\x0cgateway_list\x18\x02 \x03(\x0b\x32\x19.poktroll.gateway.GatewayB\x04\xc8\xde\x1f\x00R\x0bgatewayListB6Z0github.com/pokt-network/poktroll/x/gateway/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'poktroll.gateway.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z0github.com/pokt-network/poktroll/x/gateway/types\330\342\036\001'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['gateway_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['gateway_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=155
  _globals['_GENESISSTATE']._serialized_end=298
# @@protoc_insertion_point(module_scope)