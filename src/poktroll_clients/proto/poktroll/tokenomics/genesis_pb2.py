# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: poktroll/tokenomics/genesis.proto
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
    'poktroll/tokenomics/genesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from poktroll_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from poktroll_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from poktroll_clients.proto.poktroll.tokenomics import params_pb2 as poktroll_dot_tokenomics_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!poktroll/tokenomics/genesis.proto\x12\x13poktroll.tokenomics\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a poktroll/tokenomics/params.proto\"N\n\x0cGenesisState\x12>\n\x06params\x18\x01 \x01(\x0b\x32\x1b.poktroll.tokenomics.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06paramsB9Z3github.com/pokt-network/poktroll/x/tokenomics/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'poktroll.tokenomics.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/pokt-network/poktroll/x/tokenomics/types\330\342\036\001'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE']._serialized_start=133
  _globals['_GENESISSTATE']._serialized_end=211
# @@protoc_insertion_point(module_scope)
