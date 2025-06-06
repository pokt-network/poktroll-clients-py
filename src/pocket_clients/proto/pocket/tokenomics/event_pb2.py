# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pocket/tokenomics/event.proto
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
    'pocket/tokenomics/event.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pocket_clients.proto.pocket.proof import types_pb2 as pocket_dot_proof_dot_types__pb2
from pocket_clients.proto.pocket.tokenomics import types_pb2 as pocket_dot_tokenomics_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dpocket/tokenomics/event.proto\x12\x11pocket.tokenomics\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x18pocket/proof/types.proto\x1a\x1dpocket/tokenomics/types.proto\"\xf3\x03\n\x11\x45ventClaimExpired\x12\x34\n\x05\x63laim\x18\x01 \x01(\x0b\x32\x13.pocket.proof.ClaimB\t\xea\xde\x1f\x05\x63laimR\x05\x63laim\x12l\n\x11\x65xpiration_reason\x18\x02 \x01(\x0e\x32(.pocket.tokenomics.ClaimExpirationReasonB\x15\xea\xde\x1f\x11\x65xpiration_reasonR\x10\x65xpirationReason\x12-\n\nnum_relays\x18\x03 \x01(\x04\x42\x0e\xea\xde\x1f\nnum_relaysR\tnumRelays\x12X\n\x19num_claimed_compute_units\x18\x04 \x01(\x04\x42\x1d\xea\xde\x1f\x19num_claimed_compute_unitsR\x16numClaimedComputeUnits\x12^\n\x1bnum_estimated_compute_units\x18\x05 \x01(\x04\x42\x1f\xea\xde\x1f\x1bnum_estimated_compute_unitsR\x18numEstimatedComputeUnits\x12Q\n\rclaimed_upokt\x18\x06 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x11\xea\xde\x1f\rclaimed_upoktR\x0c\x63laimedUpokt\"\xe1\x04\n\x11\x45ventClaimSettled\x12\x34\n\x05\x63laim\x18\x01 \x01(\x0b\x32\x13.pocket.proof.ClaimB\t\xea\xde\x1f\x05\x63laimR\x05\x63laim\x12h\n\x11proof_requirement\x18\x02 \x01(\x0e\x32$.pocket.proof.ProofRequirementReasonB\x15\xea\xde\x1f\x11proof_requirementR\x10proofRequirement\x12-\n\nnum_relays\x18\x03 \x01(\x04\x42\x0e\xea\xde\x1f\nnum_relaysR\tnumRelays\x12X\n\x19num_claimed_compute_units\x18\x04 \x01(\x04\x42\x1d\xea\xde\x1f\x19num_claimed_compute_unitsR\x16numClaimedComputeUnits\x12^\n\x1bnum_estimated_compute_units\x18\x05 \x01(\x04\x42\x1f\xea\xde\x1f\x1bnum_estimated_compute_unitsR\x18numEstimatedComputeUnits\x12Q\n\rclaimed_upokt\x18\x06 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x11\xea\xde\x1f\rclaimed_upoktR\x0c\x63laimedUpokt\x12p\n\x11settlement_result\x18\x07 \x01(\x0b\x32(.pocket.tokenomics.ClaimSettlementResultB\x19\xc8\xde\x1f\x00\xea\xde\x1f\x11settlement_resultR\x10settlementResult\"\x81\x02\n\x1c\x45ventApplicationOverserviced\x12)\n\x10\x61pplication_addr\x18\x01 \x01(\tR\x0f\x61pplicationAddr\x12\x34\n\x16supplier_operator_addr\x18\x02 \x01(\tR\x14supplierOperatorAddr\x12>\n\rexpected_burn\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x0c\x65xpectedBurn\x12@\n\x0e\x65\x66\x66\x65\x63tive_burn\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\reffectiveBurn\"\x90\x01\n\x14\x45ventSupplierSlashed\x12)\n\x05\x63laim\x18\x01 \x01(\x0b\x32\x13.pocket.proof.ClaimR\x05\x63laim\x12M\n\x15proof_missing_penalty\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x13proofMissingPenalty\"\xa8\x02\n$EventApplicationReimbursementRequest\x12)\n\x10\x61pplication_addr\x18\x01 \x01(\tR\x0f\x61pplicationAddr\x12\x34\n\x16supplier_operator_addr\x18\x02 \x01(\tR\x14supplierOperatorAddr\x12.\n\x13supplier_owner_addr\x18\x03 \x01(\tR\x11supplierOwnerAddr\x12\x1d\n\nservice_id\x18\x04 \x01(\tR\tserviceId\x12\x1d\n\nsession_id\x18\x05 \x01(\tR\tsessionId\x12\x31\n\x06\x61mount\x18\x06 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x06\x61mount*`\n\x15\x43laimExpirationReason\x12!\n\x1d\x45XPIRATION_REASON_UNSPECIFIED\x10\x00\x12\x11\n\rPROOF_MISSING\x10\x01\x12\x11\n\rPROOF_INVALID\x10\x02\x42\x39Z3github.com/pokt-network/poktroll/x/tokenomics/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pocket.tokenomics.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/pokt-network/poktroll/x/tokenomics/types\330\342\036\001'
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['claim']._loaded_options = None
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['claim']._serialized_options = b'\352\336\037\005claim'
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['expiration_reason']._loaded_options = None
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['expiration_reason']._serialized_options = b'\352\336\037\021expiration_reason'
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['num_relays']._loaded_options = None
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['num_relays']._serialized_options = b'\352\336\037\nnum_relays'
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['num_claimed_compute_units']._loaded_options = None
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['num_claimed_compute_units']._serialized_options = b'\352\336\037\031num_claimed_compute_units'
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['num_estimated_compute_units']._loaded_options = None
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['num_estimated_compute_units']._serialized_options = b'\352\336\037\033num_estimated_compute_units'
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['claimed_upokt']._loaded_options = None
  _globals['_EVENTCLAIMEXPIRED'].fields_by_name['claimed_upokt']._serialized_options = b'\352\336\037\rclaimed_upokt'
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['claim']._loaded_options = None
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['claim']._serialized_options = b'\352\336\037\005claim'
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['proof_requirement']._loaded_options = None
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['proof_requirement']._serialized_options = b'\352\336\037\021proof_requirement'
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['num_relays']._loaded_options = None
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['num_relays']._serialized_options = b'\352\336\037\nnum_relays'
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['num_claimed_compute_units']._loaded_options = None
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['num_claimed_compute_units']._serialized_options = b'\352\336\037\031num_claimed_compute_units'
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['num_estimated_compute_units']._loaded_options = None
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['num_estimated_compute_units']._serialized_options = b'\352\336\037\033num_estimated_compute_units'
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['claimed_upokt']._loaded_options = None
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['claimed_upokt']._serialized_options = b'\352\336\037\rclaimed_upokt'
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['settlement_result']._loaded_options = None
  _globals['_EVENTCLAIMSETTLED'].fields_by_name['settlement_result']._serialized_options = b'\310\336\037\000\352\336\037\021settlement_result'
  _globals['_CLAIMEXPIRATIONREASON']._serialized_start=1983
  _globals['_CLAIMEXPIRATIONREASON']._serialized_end=2079
  _globals['_EVENTCLAIMEXPIRED']._serialized_start=164
  _globals['_EVENTCLAIMEXPIRED']._serialized_end=663
  _globals['_EVENTCLAIMSETTLED']._serialized_start=666
  _globals['_EVENTCLAIMSETTLED']._serialized_end=1275
  _globals['_EVENTAPPLICATIONOVERSERVICED']._serialized_start=1278
  _globals['_EVENTAPPLICATIONOVERSERVICED']._serialized_end=1535
  _globals['_EVENTSUPPLIERSLASHED']._serialized_start=1538
  _globals['_EVENTSUPPLIERSLASHED']._serialized_end=1682
  _globals['_EVENTAPPLICATIONREIMBURSEMENTREQUEST']._serialized_start=1685
  _globals['_EVENTAPPLICATIONREIMBURSEMENTREQUEST']._serialized_end=1981
# @@protoc_insertion_point(module_scope)
