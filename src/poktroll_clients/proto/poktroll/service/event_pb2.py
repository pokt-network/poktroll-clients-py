# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: poktroll/service/event.proto
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
    'poktroll/service/event.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from poktroll_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cpoktroll/service/event.proto\x12\x10poktroll.service\x1a\x14gogoproto/gogo.proto\"\x9c\x02\n!EventRelayMiningDifficultyUpdated\x12\x1d\n\nservice_id\x18\x01 \x01(\tR\tserviceId\x12>\n\x1cprev_target_hash_hex_encoded\x18\x02 \x01(\tR\x18prevTargetHashHexEncoded\x12<\n\x1bnew_target_hash_hex_encoded\x18\x03 \x01(\tR\x17newTargetHashHexEncoded\x12-\n\x13prev_num_relays_ema\x18\x04 \x01(\x04R\x10prevNumRelaysEma\x12+\n\x12new_num_relays_ema\x18\x05 \x01(\x04R\x0fnewNumRelaysEmaB6Z0github.com/pokt-network/poktroll/x/service/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'poktroll.service.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z0github.com/pokt-network/poktroll/x/service/types\330\342\036\001'
  _globals['_EVENTRELAYMININGDIFFICULTYUPDATED']._serialized_start=73
  _globals['_EVENTRELAYMININGDIFFICULTYUPDATED']._serialized_end=357
# @@protoc_insertion_point(module_scope)
