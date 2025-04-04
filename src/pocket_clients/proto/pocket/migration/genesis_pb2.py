# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pocket/migration/genesis.proto
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
    'pocket/migration/genesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pocket_clients.proto.pocket.migration import params_pb2 as pocket_dot_migration_dot_params__pb2
from pocket_clients.proto.pocket.migration import morse_onchain_pb2 as pocket_dot_migration_dot_morse__onchain__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epocket/migration/genesis.proto\x12\x10pocket.migration\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1dpocket/migration/params.proto\x1a$pocket/migration/morse_onchain.proto\"\xb8\x01\n\x0cGenesisState\x12;\n\x06params\x18\x01 \x01(\x0b\x32\x18.pocket.migration.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params\x12k\n\x19morseClaimableAccountList\x18\x02 \x03(\x0b\x32\'.pocket.migration.MorseClaimableAccountB\x04\xc8\xde\x1f\x00R\x19morseClaimableAccountListB8Z2github.com/pokt-network/poktroll/x/migration/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pocket.migration.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/pokt-network/poktroll/x/migration/types\330\342\036\001'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['morseClaimableAccountList']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['morseClaimableAccountList']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=163
  _globals['_GENESISSTATE']._serialized_end=347
# @@protoc_insertion_point(module_scope)
