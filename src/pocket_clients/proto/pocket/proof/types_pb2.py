# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pocket/proof/types.proto
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
    'pocket/proof/types.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pocket_clients.proto.pocket.session import types_pb2 as pocket_dot_session_dot_types__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18pocket/proof/types.proto\x12\x0cpocket.proof\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1apocket/session/types.proto\x1a\x14gogoproto/gogo.proto\"\xd5\x01\n\x05Proof\x12T\n\x19supplier_operator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x17supplierOperatorAddress\x12\x44\n\x0esession_header\x18\x02 \x01(\x0b\x32\x1d.pocket.session.SessionHeaderR\rsessionHeader\x12\x30\n\x14\x63losest_merkle_proof\x18\x03 \x01(\x0cR\x12\x63losestMerkleProof\"\x98\x02\n\x05\x43laim\x12T\n\x19supplier_operator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x17supplierOperatorAddress\x12\x44\n\x0esession_header\x18\x02 \x01(\x0b\x32\x1d.pocket.session.SessionHeaderR\rsessionHeader\x12\x1b\n\troot_hash\x18\x03 \x01(\x0cR\x08rootHash\x12V\n\x17proof_validation_status\x18\x04 \x01(\x0e\x32\x1e.pocket.proof.ClaimProofStatusR\x15proofValidationStatus\"\xc3\x01\n\nSessionSMT\x12\x44\n\x0esession_header\x18\x01 \x01(\x0b\x32\x1d.pocket.session.SessionHeaderR\rsessionHeader\x12T\n\x19supplier_operator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x17supplierOperatorAddress\x12\x19\n\x08smt_root\x18\x03 \x01(\x0cR\x07smtRoot*L\n\x16ProofRequirementReason\x12\x10\n\x0cNOT_REQUIRED\x10\x00\x12\x11\n\rPROBABILISTIC\x10\x01\x12\r\n\tTHRESHOLD\x10\x02*D\n\x0f\x43laimProofStage\x12\x0b\n\x07\x43LAIMED\x10\x00\x12\n\n\x06PROVEN\x10\x01\x12\x0b\n\x07SETTLED\x10\x02\x12\x0b\n\x07\x45XPIRED\x10\x03*F\n\x10\x43laimProofStatus\x12\x16\n\x12PENDING_VALIDATION\x10\x00\x12\r\n\tVALIDATED\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x42\x34Z.github.com/pokt-network/poktroll/x/proof/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pocket.proof.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z.github.com/pokt-network/poktroll/x/proof/types\330\342\036\001'
  _globals['_PROOF'].fields_by_name['supplier_operator_address']._loaded_options = None
  _globals['_PROOF'].fields_by_name['supplier_operator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_CLAIM'].fields_by_name['supplier_operator_address']._loaded_options = None
  _globals['_CLAIM'].fields_by_name['supplier_operator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_SESSIONSMT'].fields_by_name['supplier_operator_address']._loaded_options = None
  _globals['_SESSIONSMT'].fields_by_name['supplier_operator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_PROOFREQUIREMENTREASON']._serialized_start=816
  _globals['_PROOFREQUIREMENTREASON']._serialized_end=892
  _globals['_CLAIMPROOFSTAGE']._serialized_start=894
  _globals['_CLAIMPROOFSTAGE']._serialized_end=962
  _globals['_CLAIMPROOFSTATUS']._serialized_start=964
  _globals['_CLAIMPROOFSTATUS']._serialized_end=1034
  _globals['_PROOF']._serialized_start=120
  _globals['_PROOF']._serialized_end=333
  _globals['_CLAIM']._serialized_start=336
  _globals['_CLAIM']._serialized_end=616
  _globals['_SESSIONSMT']._serialized_start=619
  _globals['_SESSIONSMT']._serialized_end=814
# @@protoc_insertion_point(module_scope)
