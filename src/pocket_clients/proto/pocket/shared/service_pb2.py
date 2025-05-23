# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pocket/shared/service.proto
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
    'pocket/shared/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bpocket/shared/service.proto\x12\rpocket.shared\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\"\xa3\x01\n\x07Service\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x35\n\x17\x63ompute_units_per_relay\x18\x03 \x01(\x04R\x14\x63omputeUnitsPerRelay\x12=\n\rowner_address\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0cownerAddress\"9\n\x18\x41pplicationServiceConfig\x12\x1d\n\nservice_id\x18\x01 \x01(\tR\tserviceId\"\xb6\x01\n\x15SupplierServiceConfig\x12\x1d\n\nservice_id\x18\x01 \x01(\tR\tserviceId\x12=\n\tendpoints\x18\x02 \x03(\x0b\x32\x1f.pocket.shared.SupplierEndpointR\tendpoints\x12?\n\trev_share\x18\x03 \x03(\x0b\x32\".pocket.shared.ServiceRevenueShareR\x08revShare\"\x8e\x01\n\x10SupplierEndpoint\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x31\n\x08rpc_type\x18\x02 \x01(\x0e\x32\x16.pocket.shared.RPCTypeR\x07rpcType\x12\x35\n\x07\x63onfigs\x18\x03 \x03(\x0b\x32\x1b.pocket.shared.ConfigOptionR\x07\x63onfigs\"\x81\x01\n\x13ServiceRevenueShare\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x30\n\x14rev_share_percentage\x18\x03 \x01(\x04R\x12revSharePercentageJ\x04\x08\x02\x10\x03\"T\n\x0c\x43onfigOption\x12.\n\x03key\x18\x01 \x01(\x0e\x32\x1c.pocket.shared.ConfigOptionsR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value*K\n\x07RPCType\x12\x0f\n\x0bUNKNOWN_RPC\x10\x00\x12\x08\n\x04GRPC\x10\x01\x12\r\n\tWEBSOCKET\x10\x02\x12\x0c\n\x08JSON_RPC\x10\x03\x12\x08\n\x04REST\x10\x04*0\n\rConfigOptions\x12\x12\n\x0eUNKNOWN_CONFIG\x10\x00\x12\x0b\n\x07TIMEOUT\x10\x01\x42\x35Z/github.com/pokt-network/poktroll/x/shared/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pocket.shared.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z/github.com/pokt-network/poktroll/x/shared/types\330\342\036\001'
  _globals['_SERVICE'].fields_by_name['owner_address']._loaded_options = None
  _globals['_SERVICE'].fields_by_name['owner_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_SERVICEREVENUESHARE'].fields_by_name['address']._loaded_options = None
  _globals['_SERVICEREVENUESHARE'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_RPCTYPE']._serialized_start=868
  _globals['_RPCTYPE']._serialized_end=943
  _globals['_CONFIGOPTIONS']._serialized_start=945
  _globals['_CONFIGOPTIONS']._serialized_end=993
  _globals['_SERVICE']._serialized_start=96
  _globals['_SERVICE']._serialized_end=259
  _globals['_APPLICATIONSERVICECONFIG']._serialized_start=261
  _globals['_APPLICATIONSERVICECONFIG']._serialized_end=318
  _globals['_SUPPLIERSERVICECONFIG']._serialized_start=321
  _globals['_SUPPLIERSERVICECONFIG']._serialized_end=503
  _globals['_SUPPLIERENDPOINT']._serialized_start=506
  _globals['_SUPPLIERENDPOINT']._serialized_end=648
  _globals['_SERVICEREVENUESHARE']._serialized_start=651
  _globals['_SERVICEREVENUESHARE']._serialized_end=780
  _globals['_CONFIGOPTION']._serialized_start=782
  _globals['_CONFIGOPTION']._serialized_end=866
# @@protoc_insertion_point(module_scope)
