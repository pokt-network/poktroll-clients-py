# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pocket/proof/query.proto
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
    'pocket/proof/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pocket_clients.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pocket_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pocket_clients.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pocket_clients.proto.pocket.proof import params_pb2 as pocket_dot_proof_dot_params__pb2
from pocket_clients.proto.pocket.proof import types_pb2 as pocket_dot_proof_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18pocket/proof/query.proto\x12\x0cpocket.proof\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x19pocket/proof/params.proto\x1a\x18pocket/proof/types.proto\"\x14\n\x12QueryParamsRequest\"N\n\x13QueryParamsResponse\x12\x37\n\x06params\x18\x01 \x01(\x0b\x32\x14.pocket.proof.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params\"\x8b\x01\n\x14QueryGetClaimRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\x12T\n\x19supplier_operator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x17supplierOperatorAddress\"H\n\x15QueryGetClaimResponse\x12/\n\x05\x63laim\x18\x01 \x01(\x0b\x32\x13.pocket.proof.ClaimB\x04\xc8\xde\x1f\x00R\x05\x63laim\"\xf8\x01\n\x15QueryAllClaimsRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\x12<\n\x19supplier_operator_address\x18\x02 \x01(\tH\x00R\x17supplierOperatorAddress\x12\x1f\n\nsession_id\x18\x03 \x01(\tH\x00R\tsessionId\x12.\n\x12session_end_height\x18\x04 \x01(\x04H\x00R\x10sessionEndHeightB\x08\n\x06\x66ilter\"\x94\x01\n\x16QueryAllClaimsResponse\x12\x31\n\x06\x63laims\x18\x01 \x03(\x0b\x32\x13.pocket.proof.ClaimB\x04\xc8\xde\x1f\x00R\x06\x63laims\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\x8b\x01\n\x14QueryGetProofRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\x12T\n\x19supplier_operator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x17supplierOperatorAddress\"H\n\x15QueryGetProofResponse\x12/\n\x05proof\x18\x01 \x01(\x0b\x32\x13.pocket.proof.ProofB\x04\xc8\xde\x1f\x00R\x05proof\"\xf8\x01\n\x15QueryAllProofsRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\x12<\n\x19supplier_operator_address\x18\x02 \x01(\tH\x00R\x17supplierOperatorAddress\x12\x1f\n\nsession_id\x18\x03 \x01(\tH\x00R\tsessionId\x12.\n\x12session_end_height\x18\x04 \x01(\x04H\x00R\x10sessionEndHeightB\x08\n\x06\x66ilter\"\x94\x01\n\x16QueryAllProofsResponse\x12\x31\n\x06proofs\x18\x01 \x03(\x0b\x32\x13.pocket.proof.ProofB\x04\xc8\xde\x1f\x00R\x06proofs\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination2\xdd\x05\n\x05Query\x12z\n\x06Params\x12 .pocket.proof.QueryParamsRequest\x1a!.pocket.proof.QueryParamsResponse\"+\x82\xd3\xe4\x93\x02%\x12#/pokt-network/poktroll/proof/params\x12\xa5\x01\n\x05\x43laim\x12\".pocket.proof.QueryGetClaimRequest\x1a#.pocket.proof.QueryGetClaimResponse\"S\x82\xd3\xe4\x93\x02M\x12K/pokt-network/poktroll/proof/claim/{session_id}/{supplier_operator_address}\x12\x82\x01\n\tAllClaims\x12#.pocket.proof.QueryAllClaimsRequest\x1a$.pocket.proof.QueryAllClaimsResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/pokt-network/poktroll/proof/claim\x12\xa5\x01\n\x05Proof\x12\".pocket.proof.QueryGetProofRequest\x1a#.pocket.proof.QueryGetProofResponse\"S\x82\xd3\xe4\x93\x02M\x12K/pokt-network/poktroll/proof/proof/{session_id}/{supplier_operator_address}\x12\x82\x01\n\tAllProofs\x12#.pocket.proof.QueryAllProofsRequest\x1a$.pocket.proof.QueryAllProofsResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/pokt-network/poktroll/proof/proofB4Z.github.com/pokt-network/poktroll/x/proof/types\xd8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pocket.proof.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z.github.com/pokt-network/poktroll/x/proof/types\330\342\036\001'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERYGETCLAIMREQUEST'].fields_by_name['supplier_operator_address']._loaded_options = None
  _globals['_QUERYGETCLAIMREQUEST'].fields_by_name['supplier_operator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYGETCLAIMRESPONSE'].fields_by_name['claim']._loaded_options = None
  _globals['_QUERYGETCLAIMRESPONSE'].fields_by_name['claim']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLCLAIMSRESPONSE'].fields_by_name['claims']._loaded_options = None
  _globals['_QUERYALLCLAIMSRESPONSE'].fields_by_name['claims']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYGETPROOFREQUEST'].fields_by_name['supplier_operator_address']._loaded_options = None
  _globals['_QUERYGETPROOFREQUEST'].fields_by_name['supplier_operator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYGETPROOFRESPONSE'].fields_by_name['proof']._loaded_options = None
  _globals['_QUERYGETPROOFRESPONSE'].fields_by_name['proof']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLPROOFSRESPONSE'].fields_by_name['proofs']._loaded_options = None
  _globals['_QUERYALLPROOFSRESPONSE'].fields_by_name['proofs']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002%\022#/pokt-network/poktroll/proof/params'
  _globals['_QUERY'].methods_by_name['Claim']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Claim']._serialized_options = b'\202\323\344\223\002M\022K/pokt-network/poktroll/proof/claim/{session_id}/{supplier_operator_address}'
  _globals['_QUERY'].methods_by_name['AllClaims']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllClaims']._serialized_options = b'\202\323\344\223\002$\022\"/pokt-network/poktroll/proof/claim'
  _globals['_QUERY'].methods_by_name['Proof']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Proof']._serialized_options = b'\202\323\344\223\002M\022K/pokt-network/poktroll/proof/proof/{session_id}/{supplier_operator_address}'
  _globals['_QUERY'].methods_by_name['AllProofs']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllProofs']._serialized_options = b'\202\323\344\223\002$\022\"/pokt-network/poktroll/proof/proof'
  _globals['_QUERYPARAMSREQUEST']._serialized_start=237
  _globals['_QUERYPARAMSREQUEST']._serialized_end=257
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=259
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=337
  _globals['_QUERYGETCLAIMREQUEST']._serialized_start=340
  _globals['_QUERYGETCLAIMREQUEST']._serialized_end=479
  _globals['_QUERYGETCLAIMRESPONSE']._serialized_start=481
  _globals['_QUERYGETCLAIMRESPONSE']._serialized_end=553
  _globals['_QUERYALLCLAIMSREQUEST']._serialized_start=556
  _globals['_QUERYALLCLAIMSREQUEST']._serialized_end=804
  _globals['_QUERYALLCLAIMSRESPONSE']._serialized_start=807
  _globals['_QUERYALLCLAIMSRESPONSE']._serialized_end=955
  _globals['_QUERYGETPROOFREQUEST']._serialized_start=958
  _globals['_QUERYGETPROOFREQUEST']._serialized_end=1097
  _globals['_QUERYGETPROOFRESPONSE']._serialized_start=1099
  _globals['_QUERYGETPROOFRESPONSE']._serialized_end=1171
  _globals['_QUERYALLPROOFSREQUEST']._serialized_start=1174
  _globals['_QUERYALLPROOFSREQUEST']._serialized_end=1422
  _globals['_QUERYALLPROOFSRESPONSE']._serialized_start=1425
  _globals['_QUERYALLPROOFSRESPONSE']._serialized_end=1573
  _globals['_QUERY']._serialized_start=1576
  _globals['_QUERY']._serialized_end=2309
# @@protoc_insertion_point(module_scope)
