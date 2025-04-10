# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pocket/supplier/event.proto
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
    'pocket/supplier/event.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pocket_clients.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pocket_clients.proto.pocket.shared import supplier_pb2 as pocket_dot_shared_dot_supplier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bpocket/supplier/event.proto\x12\x0fpocket.supplier\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1cpocket/shared/supplier.proto\"\x9e\x01\n\x13\x45ventSupplierStaked\x12\x41\n\x08supplier\x18\x01 \x01(\x0b\x32\x17.pocket.shared.SupplierB\x0c\xea\xde\x1f\x08supplierR\x08supplier\x12\x44\n\x12session_end_height\x18\x02 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\"\xc0\x02\n\x1b\x45ventSupplierUnbondingBegin\x12\x41\n\x08supplier\x18\x01 \x01(\x0b\x32\x17.pocket.shared.SupplierB\x0c\xea\xde\x1f\x08supplierR\x08supplier\x12L\n\x06reason\x18\x02 \x01(\x0e\x32(.pocket.supplier.SupplierUnbondingReasonB\n\xea\xde\x1f\x06reasonR\x06reason\x12\x44\n\x12session_end_height\x18\x03 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\x12J\n\x14unbonding_end_height\x18\x04 \x01(\x03\x42\x18\xea\xde\x1f\x14unbonding_end_heightR\x12unbondingEndHeight\"\xbe\x02\n\x19\x45ventSupplierUnbondingEnd\x12\x41\n\x08supplier\x18\x01 \x01(\x0b\x32\x17.pocket.shared.SupplierB\x0c\xea\xde\x1f\x08supplierR\x08supplier\x12L\n\x06reason\x18\x02 \x01(\x0e\x32(.pocket.supplier.SupplierUnbondingReasonB\n\xea\xde\x1f\x06reasonR\x06reason\x12\x44\n\x12session_end_height\x18\x03 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\x12J\n\x14unbonding_end_height\x18\x04 \x01(\x03\x42\x18\xea\xde\x1f\x14unbonding_end_heightR\x12unbondingEndHeight\"\xcd\x01\n\x1e\x45ventSupplierUnbondingCanceled\x12\x41\n\x08supplier\x18\x01 \x01(\x0b\x32\x17.pocket.shared.SupplierB\x0c\xea\xde\x1f\x08supplierR\x08supplier\x12\"\n\x06height\x18\x03 \x01(\x03\x42\n\xea\xde\x1f\x06heightR\x06height\x12\x44\n\x12session_end_height\x18\x02 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\"\xac\x01\n#EventSupplierServiceConfigActivated\x12\x41\n\x08supplier\x18\x01 \x01(\x0b\x32\x17.pocket.shared.SupplierB\x0c\xea\xde\x1f\x08supplierR\x08supplier\x12\x42\n\x11\x61\x63tivation_height\x18\x02 \x01(\x03\x42\x15\xea\xde\x1f\x11\x61\x63tivation_heightR\x10\x61\x63tivationHeight*\x9c\x01\n\x17SupplierUnbondingReason\x12)\n%SUPPLIER_UNBONDING_REASON_UNSPECIFIED\x10\x00\x12\'\n#SUPPLIER_UNBONDING_REASON_VOLUNTARY\x10\x01\x12-\n)SUPPLIER_UNBONDING_REASON_BELOW_MIN_STAKE\x10\x02\x42\x37Z1github.com/pokt-network/poktroll/x/supplier/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pocket.supplier.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/pokt-network/poktroll/x/supplier/types\330\342\036\001'
  _globals['_EVENTSUPPLIERSTAKED'].fields_by_name['supplier']._loaded_options = None
  _globals['_EVENTSUPPLIERSTAKED'].fields_by_name['supplier']._serialized_options = b'\352\336\037\010supplier'
  _globals['_EVENTSUPPLIERSTAKED'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTSUPPLIERSTAKED'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN'].fields_by_name['supplier']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN'].fields_by_name['supplier']._serialized_options = b'\352\336\037\010supplier'
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN'].fields_by_name['reason']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN'].fields_by_name['reason']._serialized_options = b'\352\336\037\006reason'
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN'].fields_by_name['unbonding_end_height']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN'].fields_by_name['unbonding_end_height']._serialized_options = b'\352\336\037\024unbonding_end_height'
  _globals['_EVENTSUPPLIERUNBONDINGEND'].fields_by_name['supplier']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGEND'].fields_by_name['supplier']._serialized_options = b'\352\336\037\010supplier'
  _globals['_EVENTSUPPLIERUNBONDINGEND'].fields_by_name['reason']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGEND'].fields_by_name['reason']._serialized_options = b'\352\336\037\006reason'
  _globals['_EVENTSUPPLIERUNBONDINGEND'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGEND'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTSUPPLIERUNBONDINGEND'].fields_by_name['unbonding_end_height']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGEND'].fields_by_name['unbonding_end_height']._serialized_options = b'\352\336\037\024unbonding_end_height'
  _globals['_EVENTSUPPLIERUNBONDINGCANCELED'].fields_by_name['supplier']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGCANCELED'].fields_by_name['supplier']._serialized_options = b'\352\336\037\010supplier'
  _globals['_EVENTSUPPLIERUNBONDINGCANCELED'].fields_by_name['height']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGCANCELED'].fields_by_name['height']._serialized_options = b'\352\336\037\006height'
  _globals['_EVENTSUPPLIERUNBONDINGCANCELED'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTSUPPLIERUNBONDINGCANCELED'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTSUPPLIERSERVICECONFIGACTIVATED'].fields_by_name['supplier']._loaded_options = None
  _globals['_EVENTSUPPLIERSERVICECONFIGACTIVATED'].fields_by_name['supplier']._serialized_options = b'\352\336\037\010supplier'
  _globals['_EVENTSUPPLIERSERVICECONFIGACTIVATED'].fields_by_name['activation_height']._loaded_options = None
  _globals['_EVENTSUPPLIERSERVICECONFIGACTIVATED'].fields_by_name['activation_height']._serialized_options = b'\352\336\037\021activation_height'
  _globals['_SUPPLIERUNBONDINGREASON']._serialized_start=1348
  _globals['_SUPPLIERUNBONDINGREASON']._serialized_end=1504
  _globals['_EVENTSUPPLIERSTAKED']._serialized_start=160
  _globals['_EVENTSUPPLIERSTAKED']._serialized_end=318
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN']._serialized_start=321
  _globals['_EVENTSUPPLIERUNBONDINGBEGIN']._serialized_end=641
  _globals['_EVENTSUPPLIERUNBONDINGEND']._serialized_start=644
  _globals['_EVENTSUPPLIERUNBONDINGEND']._serialized_end=962
  _globals['_EVENTSUPPLIERUNBONDINGCANCELED']._serialized_start=965
  _globals['_EVENTSUPPLIERUNBONDINGCANCELED']._serialized_end=1170
  _globals['_EVENTSUPPLIERSERVICECONFIGACTIVATED']._serialized_start=1173
  _globals['_EVENTSUPPLIERSERVICECONFIGACTIVATED']._serialized_end=1345
# @@protoc_insertion_point(module_scope)
