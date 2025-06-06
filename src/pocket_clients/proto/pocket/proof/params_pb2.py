# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pocket/proof/params.proto
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
    'pocket/proof/params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pocket_clients.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19pocket/proof/params.proto\x12\x0cpocket.proof\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xd0\x03\n\x06Params\x12Y\n\x19proof_request_probability\x18\x02 \x01(\x01\x42\x1d\xea\xde\x1f\x19proof_request_probabilityR\x17proofRequestProbability\x12z\n\x1bproof_requirement_threshold\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x1f\xea\xde\x1f\x1bproof_requirement_thresholdR\x19proofRequirementThreshold\x12h\n\x15proof_missing_penalty\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x19\xea\xde\x1f\x15proof_missing_penaltyR\x13proofMissingPenalty\x12\x65\n\x14proof_submission_fee\x18\x05 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x18\xea\xde\x1f\x14proof_submission_feeR\x12proofSubmissionFee:\x1e\xe8\xa0\x1f\x01\x8a\xe7\xb0*\x15pocket/x/proof/ParamsB4Z.github.com/pokt-network/poktroll/x/proof/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pocket.proof.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z.github.com/pokt-network/poktroll/x/proof/types\330\342\036\001'
  _globals['_PARAMS'].fields_by_name['proof_request_probability']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['proof_request_probability']._serialized_options = b'\352\336\037\031proof_request_probability'
  _globals['_PARAMS'].fields_by_name['proof_requirement_threshold']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['proof_requirement_threshold']._serialized_options = b'\352\336\037\033proof_requirement_threshold'
  _globals['_PARAMS'].fields_by_name['proof_missing_penalty']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['proof_missing_penalty']._serialized_options = b'\352\336\037\025proof_missing_penalty'
  _globals['_PARAMS'].fields_by_name['proof_submission_fee']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['proof_submission_fee']._serialized_options = b'\352\336\037\024proof_submission_fee'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\350\240\037\001\212\347\260*\025pocket/x/proof/Params'
  _globals['_PARAMS']._serialized_start=117
  _globals['_PARAMS']._serialized_end=581
# @@protoc_insertion_point(module_scope)
