# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: poktroll/service/genesis.proto
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
    'poktroll/service/genesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from poktroll_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from poktroll_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from poktroll_clients.proto.poktroll.service import params_pb2 as poktroll_dot_service_dot_params__pb2
from poktroll_clients.proto.poktroll.shared import service_pb2 as poktroll_dot_shared_dot_service__pb2
from poktroll_clients.proto.poktroll.service import relay_mining_difficulty_pb2 as poktroll_dot_service_dot_relay__mining__difficulty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epoktroll/service/genesis.proto\x12\x10poktroll.service\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1dpoktroll/service/params.proto\x1a\x1dpoktroll/shared/service.proto\x1a.poktroll/service/relay_mining_difficulty.proto\"\xfb\x01\n\x0cGenesisState\x12;\n\x06params\x18\x01 \x01(\x0b\x32\x18.poktroll.service.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params\x12\x41\n\x0cservice_list\x18\x02 \x03(\x0b\x32\x18.poktroll.shared.ServiceB\x04\xc8\xde\x1f\x00R\x0bserviceList\x12k\n\x19relayMiningDifficultyList\x18\x03 \x03(\x0b\x32\'.poktroll.service.RelayMiningDifficultyB\x04\xc8\xde\x1f\x00R\x19relayMiningDifficultyListB6Z0github.com/pokt-network/poktroll/x/service/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'poktroll.service.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z0github.com/pokt-network/poktroll/x/service/types\330\342\036\001'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['service_list']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['service_list']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['relayMiningDifficultyList']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['relayMiningDifficultyList']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=204
  _globals['_GENESISSTATE']._serialized_end=455
# @@protoc_insertion_point(module_scope)