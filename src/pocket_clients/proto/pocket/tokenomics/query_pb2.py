# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pocket/tokenomics/query.proto
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
    'pocket/tokenomics/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pocket_clients.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pocket_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pocket_clients.proto.pocket.tokenomics import params_pb2 as pocket_dot_tokenomics_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dpocket/tokenomics/query.proto\x12\x11pocket.tokenomics\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1epocket/tokenomics/params.proto\"\x14\n\x12QueryParamsRequest\"S\n\x13QueryParamsResponse\x12<\n\x06params\x18\x01 \x01(\x0b\x32\x19.pocket.tokenomics.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params2\x93\x01\n\x05Query\x12\x89\x01\n\x06Params\x12%.pocket.tokenomics.QueryParamsRequest\x1a&.pocket.tokenomics.QueryParamsResponse\"0\x82\xd3\xe4\x93\x02*\x12(/pokt-network/poktroll/tokenomics/paramsB9Z3github.com/pokt-network/poktroll/x/tokenomics/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pocket.tokenomics.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/pokt-network/poktroll/x/tokenomics/types\330\342\036\001'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002*\022(/pokt-network/poktroll/tokenomics/params'
  _globals['_QUERYPARAMSREQUEST']._serialized_start=182
  _globals['_QUERYPARAMSREQUEST']._serialized_end=202
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=204
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=287
  _globals['_QUERY']._serialized_start=290
  _globals['_QUERY']._serialized_end=437
# @@protoc_insertion_point(module_scope)
