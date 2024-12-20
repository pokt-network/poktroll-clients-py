# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: poktroll/application/event.proto
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
    'poktroll/application/event.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from poktroll_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from poktroll_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from poktroll_clients.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from poktroll_clients.proto.poktroll.shared import service_pb2 as poktroll_dot_shared_dot_service__pb2
from poktroll_clients.proto.poktroll.application import types_pb2 as poktroll_dot_application_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n poktroll/application/event.proto\x12\x14poktroll.application\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1dpoktroll/shared/service.proto\x1a poktroll/application/types.proto\"\xb4\x01\n\x16\x45ventApplicationStaked\x12T\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32!.poktroll.application.ApplicationB\x0f\xea\xde\x1f\x0b\x61pplicationR\x0b\x61pplication\x12\x44\n\x12session_end_height\x18\x02 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\"\xaf\x01\n\x11\x45ventRedelegation\x12T\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32!.poktroll.application.ApplicationB\x0f\xea\xde\x1f\x0b\x61pplicationR\x0b\x61pplication\x12\x44\n\x12session_end_height\x18\x02 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\"\x81\x03\n\x12\x45ventTransferBegin\x12?\n\x0esource_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\rsourceAddress\x12I\n\x13\x64\x65stination_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x12\x64\x65stinationAddress\x12P\n\x12source_application\x18\x03 \x01(\x0b\x32!.poktroll.application.ApplicationR\x11sourceApplication\x12\x44\n\x12session_end_height\x18\x04 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\x12G\n\x13transfer_end_height\x18\x05 \x01(\x03\x42\x17\xea\xde\x1f\x13transfer_end_heightR\x11transferEndHeight\"\x89\x03\n\x10\x45ventTransferEnd\x12?\n\x0esource_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\rsourceAddress\x12I\n\x13\x64\x65stination_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x12\x64\x65stinationAddress\x12Z\n\x17\x64\x65stination_application\x18\x03 \x01(\x0b\x32!.poktroll.application.ApplicationR\x16\x64\x65stinationApplication\x12\x44\n\x12session_end_height\x18\x04 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\x12G\n\x13transfer_end_height\x18\x05 \x01(\x03\x42\x17\xea\xde\x1f\x13transfer_end_heightR\x11transferEndHeight\"\xce\x02\n\x12\x45ventTransferError\x12?\n\x0esource_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\rsourceAddress\x12I\n\x13\x64\x65stination_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x12\x64\x65stinationAddress\x12P\n\x12source_application\x18\x03 \x01(\x0b\x32!.poktroll.application.ApplicationR\x11sourceApplication\x12\x44\n\x12session_end_height\x18\x04 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\x12\x14\n\x05\x65rror\x18\x05 \x01(\tR\x05\x65rror\"\xda\x02\n\x1e\x45ventApplicationUnbondingBegin\x12T\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32!.poktroll.application.ApplicationB\x0f\xea\xde\x1f\x0b\x61pplicationR\x0b\x61pplication\x12T\n\x06reason\x18\x02 \x01(\x0e\x32\x30.poktroll.application.ApplicationUnbondingReasonB\n\xea\xde\x1f\x06reasonR\x06reason\x12\x44\n\x12session_end_height\x18\x03 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\x12\x46\n\x14unbonding_end_height\x18\x04 \x01(\x03\x42\x14\xea\xde\x1f\x10unbonding_heightR\x12unbondingEndHeight\"\xd8\x02\n\x1c\x45ventApplicationUnbondingEnd\x12T\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32!.poktroll.application.ApplicationB\x0f\xea\xde\x1f\x0b\x61pplicationR\x0b\x61pplication\x12T\n\x06reason\x18\x02 \x01(\x0e\x32\x30.poktroll.application.ApplicationUnbondingReasonB\n\xea\xde\x1f\x06reasonR\x06reason\x12\x44\n\x12session_end_height\x18\x03 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight\x12\x46\n\x14unbonding_end_height\x18\x04 \x01(\x03\x42\x14\xea\xde\x1f\x10unbonding_heightR\x12unbondingEndHeight\"\xbf\x01\n!EventApplicationUnbondingCanceled\x12T\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32!.poktroll.application.ApplicationB\x0f\xea\xde\x1f\x0b\x61pplicationR\x0b\x61pplication\x12\x44\n\x12session_end_height\x18\x02 \x01(\x03\x42\x16\xea\xde\x1f\x12session_end_heightR\x10sessionEndHeight*y\n\x1a\x41pplicationUnbondingReason\x12)\n%APPLICATION_UNBONDING_REASON_ELECTIVE\x10\x00\x12\x30\n,APPLICATION_UNBONDING_REASON_BELOW_MIN_STAKE\x10\x01\x42:Z4github.com/pokt-network/poktroll/x/application/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'poktroll.application.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/pokt-network/poktroll/x/application/types\330\342\036\001'
  _globals['_EVENTAPPLICATIONSTAKED'].fields_by_name['application']._loaded_options = None
  _globals['_EVENTAPPLICATIONSTAKED'].fields_by_name['application']._serialized_options = b'\352\336\037\013application'
  _globals['_EVENTAPPLICATIONSTAKED'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTAPPLICATIONSTAKED'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTREDELEGATION'].fields_by_name['application']._loaded_options = None
  _globals['_EVENTREDELEGATION'].fields_by_name['application']._serialized_options = b'\352\336\037\013application'
  _globals['_EVENTREDELEGATION'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTREDELEGATION'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTTRANSFERBEGIN'].fields_by_name['source_address']._loaded_options = None
  _globals['_EVENTTRANSFERBEGIN'].fields_by_name['source_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EVENTTRANSFERBEGIN'].fields_by_name['destination_address']._loaded_options = None
  _globals['_EVENTTRANSFERBEGIN'].fields_by_name['destination_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EVENTTRANSFERBEGIN'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTTRANSFERBEGIN'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTTRANSFERBEGIN'].fields_by_name['transfer_end_height']._loaded_options = None
  _globals['_EVENTTRANSFERBEGIN'].fields_by_name['transfer_end_height']._serialized_options = b'\352\336\037\023transfer_end_height'
  _globals['_EVENTTRANSFEREND'].fields_by_name['source_address']._loaded_options = None
  _globals['_EVENTTRANSFEREND'].fields_by_name['source_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EVENTTRANSFEREND'].fields_by_name['destination_address']._loaded_options = None
  _globals['_EVENTTRANSFEREND'].fields_by_name['destination_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EVENTTRANSFEREND'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTTRANSFEREND'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTTRANSFEREND'].fields_by_name['transfer_end_height']._loaded_options = None
  _globals['_EVENTTRANSFEREND'].fields_by_name['transfer_end_height']._serialized_options = b'\352\336\037\023transfer_end_height'
  _globals['_EVENTTRANSFERERROR'].fields_by_name['source_address']._loaded_options = None
  _globals['_EVENTTRANSFERERROR'].fields_by_name['source_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EVENTTRANSFERERROR'].fields_by_name['destination_address']._loaded_options = None
  _globals['_EVENTTRANSFERERROR'].fields_by_name['destination_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EVENTTRANSFERERROR'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTTRANSFERERROR'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN'].fields_by_name['application']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN'].fields_by_name['application']._serialized_options = b'\352\336\037\013application'
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN'].fields_by_name['reason']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN'].fields_by_name['reason']._serialized_options = b'\352\336\037\006reason'
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN'].fields_by_name['unbonding_end_height']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN'].fields_by_name['unbonding_end_height']._serialized_options = b'\352\336\037\020unbonding_height'
  _globals['_EVENTAPPLICATIONUNBONDINGEND'].fields_by_name['application']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGEND'].fields_by_name['application']._serialized_options = b'\352\336\037\013application'
  _globals['_EVENTAPPLICATIONUNBONDINGEND'].fields_by_name['reason']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGEND'].fields_by_name['reason']._serialized_options = b'\352\336\037\006reason'
  _globals['_EVENTAPPLICATIONUNBONDINGEND'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGEND'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_EVENTAPPLICATIONUNBONDINGEND'].fields_by_name['unbonding_end_height']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGEND'].fields_by_name['unbonding_end_height']._serialized_options = b'\352\336\037\020unbonding_height'
  _globals['_EVENTAPPLICATIONUNBONDINGCANCELED'].fields_by_name['application']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGCANCELED'].fields_by_name['application']._serialized_options = b'\352\336\037\013application'
  _globals['_EVENTAPPLICATIONUNBONDINGCANCELED'].fields_by_name['session_end_height']._loaded_options = None
  _globals['_EVENTAPPLICATIONUNBONDINGCANCELED'].fields_by_name['session_end_height']._serialized_options = b'\352\336\037\022session_end_height'
  _globals['_APPLICATIONUNBONDINGREASON']._serialized_start=2576
  _globals['_APPLICATIONUNBONDINGREASON']._serialized_end=2697
  _globals['_EVENTAPPLICATIONSTAKED']._serialized_start=205
  _globals['_EVENTAPPLICATIONSTAKED']._serialized_end=385
  _globals['_EVENTREDELEGATION']._serialized_start=388
  _globals['_EVENTREDELEGATION']._serialized_end=563
  _globals['_EVENTTRANSFERBEGIN']._serialized_start=566
  _globals['_EVENTTRANSFERBEGIN']._serialized_end=951
  _globals['_EVENTTRANSFEREND']._serialized_start=954
  _globals['_EVENTTRANSFEREND']._serialized_end=1347
  _globals['_EVENTTRANSFERERROR']._serialized_start=1350
  _globals['_EVENTTRANSFERERROR']._serialized_end=1684
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN']._serialized_start=1687
  _globals['_EVENTAPPLICATIONUNBONDINGBEGIN']._serialized_end=2033
  _globals['_EVENTAPPLICATIONUNBONDINGEND']._serialized_start=2036
  _globals['_EVENTAPPLICATIONUNBONDINGEND']._serialized_end=2380
  _globals['_EVENTAPPLICATIONUNBONDINGCANCELED']._serialized_start=2383
  _globals['_EVENTAPPLICATIONUNBONDINGCANCELED']._serialized_end=2574
# @@protoc_insertion_point(module_scope)
