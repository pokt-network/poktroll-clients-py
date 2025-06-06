# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/bank/v1beta1/query.proto
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
    'cosmos/bank/v1beta1/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pocket_clients.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pocket_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pocket_clients.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pocket_clients.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pocket_clients.proto.cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from pocket_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pocket_clients.proto.cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2
from pocket_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/bank/v1beta1/query.proto\x12\x13\x63osmos.bank.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1b\x63osmos/query/v1/query.proto\x1a\x11\x61mino/amino.proto\"i\n\x13QueryBalanceRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"K\n\x14QueryBalanceResponse\x12\x33\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x07\x62\x61lance\"\xc4\x01\n\x17QueryAllBalancesRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\x12#\n\rresolve_denom\x18\x03 \x01(\x08R\x0cresolveDenom:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xe2\x01\n\x18QueryAllBalancesResponse\x12}\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x08\x62\x61lances\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\xa5\x01\n\x1dQuerySpendableBalancesRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xe8\x01\n\x1eQuerySpendableBalancesResponse\x12}\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x08\x62\x61lances\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"y\n#QuerySpendableBalanceByDenomRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"[\n$QuerySpendableBalanceByDenomResponse\x12\x33\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x07\x62\x61lance\"k\n\x17QueryTotalSupplyRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xde\x01\n\x18QueryTotalSupplyResponse\x12y\n\x06supply\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x06supply\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\",\n\x14QuerySupplyOfRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\"U\n\x15QuerySupplyOfResponse\x12<\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06\x61mount\"\x14\n\x12QueryParamsRequest\"U\n\x13QueryParamsResponse\x12>\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.bank.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params\"d\n\x1aQueryDenomsMetadataRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xae\x01\n\x1bQueryDenomsMetadataResponse\x12\x46\n\tmetadatas\x18\x01 \x03(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\tmetadatas\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"1\n\x19QueryDenomMetadataRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\"b\n\x1aQueryDenomMetadataResponse\x12\x44\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x08metadata\">\n&QueryDenomMetadataByQueryStringRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\"o\n\'QueryDenomMetadataByQueryStringResponse\x12\x44\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x08metadata\"w\n\x17QueryDenomOwnersRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x80\x01\n\nDenomOwner\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12>\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07\x62\x61lance\"\xa7\x01\n\x18QueryDenomOwnersResponse\x12\x42\n\x0c\x64\x65nom_owners\x18\x01 \x03(\x0b\x32\x1f.cosmos.bank.v1beta1.DenomOwnerR\x0b\x64\x65nomOwners\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"~\n\x1eQueryDenomOwnersByQueryRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xae\x01\n\x1fQueryDenomOwnersByQueryResponse\x12\x42\n\x0c\x64\x65nom_owners\x18\x01 \x03(\x0b\x32\x1f.cosmos.bank.v1beta1.DenomOwnerR\x0b\x64\x65nomOwners\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"y\n\x17QuerySendEnabledRequest\x12\x16\n\x06\x64\x65noms\x18\x01 \x03(\tR\x06\x64\x65noms\x12\x46\n\npagination\x18\x63 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xa8\x01\n\x18QuerySendEnabledResponse\x12\x43\n\x0csend_enabled\x18\x01 \x03(\x0b\x32 .cosmos.bank.v1beta1.SendEnabledR\x0bsendEnabled\x12G\n\npagination\x18\x63 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination2\xca\x11\n\x05Query\x12\x9d\x01\n\x07\x42\x61lance\x12(.cosmos.bank.v1beta1.QueryBalanceRequest\x1a).cosmos.bank.v1beta1.QueryBalanceResponse\"=\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x32\x12\x30/cosmos/bank/v1beta1/balances/{address}/by_denom\x12\xa0\x01\n\x0b\x41llBalances\x12,.cosmos.bank.v1beta1.QueryAllBalancesRequest\x1a-.cosmos.bank.v1beta1.QueryAllBalancesResponse\"4\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02)\x12\'/cosmos/bank/v1beta1/balances/{address}\x12\xbc\x01\n\x11SpendableBalances\x12\x32.cosmos.bank.v1beta1.QuerySpendableBalancesRequest\x1a\x33.cosmos.bank.v1beta1.QuerySpendableBalancesResponse\">\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x33\x12\x31/cosmos/bank/v1beta1/spendable_balances/{address}\x12\xd7\x01\n\x17SpendableBalanceByDenom\x12\x38.cosmos.bank.v1beta1.QuerySpendableBalanceByDenomRequest\x1a\x39.cosmos.bank.v1beta1.QuerySpendableBalanceByDenomResponse\"G\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02<\x12:/cosmos/bank/v1beta1/spendable_balances/{address}/by_denom\x12\x94\x01\n\x0bTotalSupply\x12,.cosmos.bank.v1beta1.QueryTotalSupplyRequest\x1a-.cosmos.bank.v1beta1.QueryTotalSupplyResponse\"(\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/supply\x12\x94\x01\n\x08SupplyOf\x12).cosmos.bank.v1beta1.QuerySupplyOfRequest\x1a*.cosmos.bank.v1beta1.QuerySupplyOfResponse\"1\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/supply/by_denom\x12\x85\x01\n\x06Params\x12\'.cosmos.bank.v1beta1.QueryParamsRequest\x1a(.cosmos.bank.v1beta1.QueryParamsResponse\"(\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/params\x12\xab\x01\n\rDenomMetadata\x12..cosmos.bank.v1beta1.QueryDenomMetadataRequest\x1a/.cosmos.bank.v1beta1.QueryDenomMetadataResponse\"9\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02.\x12,/cosmos/bank/v1beta1/denoms_metadata/{denom}\x12\xda\x01\n\x1a\x44\x65nomMetadataByQueryString\x12;.cosmos.bank.v1beta1.QueryDenomMetadataByQueryStringRequest\x1a<.cosmos.bank.v1beta1.QueryDenomMetadataByQueryStringResponse\"A\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x36\x12\x34/cosmos/bank/v1beta1/denoms_metadata_by_query_string\x12\xa6\x01\n\x0e\x44\x65nomsMetadata\x12/.cosmos.bank.v1beta1.QueryDenomsMetadataRequest\x1a\x30.cosmos.bank.v1beta1.QueryDenomsMetadataResponse\"1\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/denoms_metadata\x12\xa2\x01\n\x0b\x44\x65nomOwners\x12,.cosmos.bank.v1beta1.QueryDenomOwnersRequest\x1a-.cosmos.bank.v1beta1.QueryDenomOwnersResponse\"6\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02+\x12)/cosmos/bank/v1beta1/denom_owners/{denom}\x12\xb8\x01\n\x12\x44\x65nomOwnersByQuery\x12\x33.cosmos.bank.v1beta1.QueryDenomOwnersByQueryRequest\x1a\x34.cosmos.bank.v1beta1.QueryDenomOwnersByQueryResponse\"7\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02,\x12*/cosmos/bank/v1beta1/denom_owners_by_query\x12\x9a\x01\n\x0bSendEnabled\x12,.cosmos.bank.v1beta1.QuerySendEnabledRequest\x1a-.cosmos.bank.v1beta1.QuerySendEnabledResponse\".\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02#\x12!/cosmos/bank/v1beta1/send_enabledB\x1bZ\x19\x63osmossdk.io/x/bank/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\031cosmossdk.io/x/bank/types'
  _globals['_QUERYBALANCEREQUEST'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYBALANCEREQUEST'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYBALANCEREQUEST']._loaded_options = None
  _globals['_QUERYBALANCEREQUEST']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_QUERYALLBALANCESREQUEST'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYALLBALANCESREQUEST'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYALLBALANCESREQUEST']._loaded_options = None
  _globals['_QUERYALLBALANCESREQUEST']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_QUERYALLBALANCESRESPONSE'].fields_by_name['balances']._loaded_options = None
  _globals['_QUERYALLBALANCESRESPONSE'].fields_by_name['balances']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_QUERYSPENDABLEBALANCESREQUEST'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYSPENDABLEBALANCESREQUEST'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYSPENDABLEBALANCESREQUEST']._loaded_options = None
  _globals['_QUERYSPENDABLEBALANCESREQUEST']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_QUERYSPENDABLEBALANCESRESPONSE'].fields_by_name['balances']._loaded_options = None
  _globals['_QUERYSPENDABLEBALANCESRESPONSE'].fields_by_name['balances']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_QUERYSPENDABLEBALANCEBYDENOMREQUEST'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYSPENDABLEBALANCEBYDENOMREQUEST'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYSPENDABLEBALANCEBYDENOMREQUEST']._loaded_options = None
  _globals['_QUERYSPENDABLEBALANCEBYDENOMREQUEST']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_QUERYTOTALSUPPLYREQUEST']._loaded_options = None
  _globals['_QUERYTOTALSUPPLYREQUEST']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_QUERYTOTALSUPPLYRESPONSE'].fields_by_name['supply']._loaded_options = None
  _globals['_QUERYTOTALSUPPLYRESPONSE'].fields_by_name['supply']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_QUERYSUPPLYOFRESPONSE'].fields_by_name['amount']._loaded_options = None
  _globals['_QUERYSUPPLYOFRESPONSE'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERYDENOMSMETADATARESPONSE'].fields_by_name['metadatas']._loaded_options = None
  _globals['_QUERYDENOMSMETADATARESPONSE'].fields_by_name['metadatas']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERYDENOMMETADATARESPONSE'].fields_by_name['metadata']._loaded_options = None
  _globals['_QUERYDENOMMETADATARESPONSE'].fields_by_name['metadata']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERYDENOMMETADATABYQUERYSTRINGRESPONSE'].fields_by_name['metadata']._loaded_options = None
  _globals['_QUERYDENOMMETADATABYQUERYSTRINGRESPONSE'].fields_by_name['metadata']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_DENOMOWNER'].fields_by_name['address']._loaded_options = None
  _globals['_DENOMOWNER'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_DENOMOWNER'].fields_by_name['balance']._loaded_options = None
  _globals['_DENOMOWNER'].fields_by_name['balance']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERY'].methods_by_name['Balance']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Balance']._serialized_options = b'\210\347\260*\001\202\323\344\223\0022\0220/cosmos/bank/v1beta1/balances/{address}/by_denom'
  _globals['_QUERY'].methods_by_name['AllBalances']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllBalances']._serialized_options = b'\210\347\260*\001\202\323\344\223\002)\022\'/cosmos/bank/v1beta1/balances/{address}'
  _globals['_QUERY'].methods_by_name['SpendableBalances']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SpendableBalances']._serialized_options = b'\210\347\260*\001\202\323\344\223\0023\0221/cosmos/bank/v1beta1/spendable_balances/{address}'
  _globals['_QUERY'].methods_by_name['SpendableBalanceByDenom']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SpendableBalanceByDenom']._serialized_options = b'\210\347\260*\001\202\323\344\223\002<\022:/cosmos/bank/v1beta1/spendable_balances/{address}/by_denom'
  _globals['_QUERY'].methods_by_name['TotalSupply']._loaded_options = None
  _globals['_QUERY'].methods_by_name['TotalSupply']._serialized_options = b'\210\347\260*\001\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/supply'
  _globals['_QUERY'].methods_by_name['SupplyOf']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SupplyOf']._serialized_options = b'\210\347\260*\001\202\323\344\223\002&\022$/cosmos/bank/v1beta1/supply/by_denom'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\210\347\260*\001\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/params'
  _globals['_QUERY'].methods_by_name['DenomMetadata']._loaded_options = None
  _globals['_QUERY'].methods_by_name['DenomMetadata']._serialized_options = b'\210\347\260*\001\202\323\344\223\002.\022,/cosmos/bank/v1beta1/denoms_metadata/{denom}'
  _globals['_QUERY'].methods_by_name['DenomMetadataByQueryString']._loaded_options = None
  _globals['_QUERY'].methods_by_name['DenomMetadataByQueryString']._serialized_options = b'\210\347\260*\001\202\323\344\223\0026\0224/cosmos/bank/v1beta1/denoms_metadata_by_query_string'
  _globals['_QUERY'].methods_by_name['DenomsMetadata']._loaded_options = None
  _globals['_QUERY'].methods_by_name['DenomsMetadata']._serialized_options = b'\210\347\260*\001\202\323\344\223\002&\022$/cosmos/bank/v1beta1/denoms_metadata'
  _globals['_QUERY'].methods_by_name['DenomOwners']._loaded_options = None
  _globals['_QUERY'].methods_by_name['DenomOwners']._serialized_options = b'\210\347\260*\001\202\323\344\223\002+\022)/cosmos/bank/v1beta1/denom_owners/{denom}'
  _globals['_QUERY'].methods_by_name['DenomOwnersByQuery']._loaded_options = None
  _globals['_QUERY'].methods_by_name['DenomOwnersByQuery']._serialized_options = b'\210\347\260*\001\202\323\344\223\002,\022*/cosmos/bank/v1beta1/denom_owners_by_query'
  _globals['_QUERY'].methods_by_name['SendEnabled']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SendEnabled']._serialized_options = b'\210\347\260*\001\202\323\344\223\002#\022!/cosmos/bank/v1beta1/send_enabled'
  _globals['_QUERYBALANCEREQUEST']._serialized_start=291
  _globals['_QUERYBALANCEREQUEST']._serialized_end=396
  _globals['_QUERYBALANCERESPONSE']._serialized_start=398
  _globals['_QUERYBALANCERESPONSE']._serialized_end=473
  _globals['_QUERYALLBALANCESREQUEST']._serialized_start=476
  _globals['_QUERYALLBALANCESREQUEST']._serialized_end=672
  _globals['_QUERYALLBALANCESRESPONSE']._serialized_start=675
  _globals['_QUERYALLBALANCESRESPONSE']._serialized_end=901
  _globals['_QUERYSPENDABLEBALANCESREQUEST']._serialized_start=904
  _globals['_QUERYSPENDABLEBALANCESREQUEST']._serialized_end=1069
  _globals['_QUERYSPENDABLEBALANCESRESPONSE']._serialized_start=1072
  _globals['_QUERYSPENDABLEBALANCESRESPONSE']._serialized_end=1304
  _globals['_QUERYSPENDABLEBALANCEBYDENOMREQUEST']._serialized_start=1306
  _globals['_QUERYSPENDABLEBALANCEBYDENOMREQUEST']._serialized_end=1427
  _globals['_QUERYSPENDABLEBALANCEBYDENOMRESPONSE']._serialized_start=1429
  _globals['_QUERYSPENDABLEBALANCEBYDENOMRESPONSE']._serialized_end=1520
  _globals['_QUERYTOTALSUPPLYREQUEST']._serialized_start=1522
  _globals['_QUERYTOTALSUPPLYREQUEST']._serialized_end=1629
  _globals['_QUERYTOTALSUPPLYRESPONSE']._serialized_start=1632
  _globals['_QUERYTOTALSUPPLYRESPONSE']._serialized_end=1854
  _globals['_QUERYSUPPLYOFREQUEST']._serialized_start=1856
  _globals['_QUERYSUPPLYOFREQUEST']._serialized_end=1900
  _globals['_QUERYSUPPLYOFRESPONSE']._serialized_start=1902
  _globals['_QUERYSUPPLYOFRESPONSE']._serialized_end=1987
  _globals['_QUERYPARAMSREQUEST']._serialized_start=1989
  _globals['_QUERYPARAMSREQUEST']._serialized_end=2009
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=2011
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=2096
  _globals['_QUERYDENOMSMETADATAREQUEST']._serialized_start=2098
  _globals['_QUERYDENOMSMETADATAREQUEST']._serialized_end=2198
  _globals['_QUERYDENOMSMETADATARESPONSE']._serialized_start=2201
  _globals['_QUERYDENOMSMETADATARESPONSE']._serialized_end=2375
  _globals['_QUERYDENOMMETADATAREQUEST']._serialized_start=2377
  _globals['_QUERYDENOMMETADATAREQUEST']._serialized_end=2426
  _globals['_QUERYDENOMMETADATARESPONSE']._serialized_start=2428
  _globals['_QUERYDENOMMETADATARESPONSE']._serialized_end=2526
  _globals['_QUERYDENOMMETADATABYQUERYSTRINGREQUEST']._serialized_start=2528
  _globals['_QUERYDENOMMETADATABYQUERYSTRINGREQUEST']._serialized_end=2590
  _globals['_QUERYDENOMMETADATABYQUERYSTRINGRESPONSE']._serialized_start=2592
  _globals['_QUERYDENOMMETADATABYQUERYSTRINGRESPONSE']._serialized_end=2703
  _globals['_QUERYDENOMOWNERSREQUEST']._serialized_start=2705
  _globals['_QUERYDENOMOWNERSREQUEST']._serialized_end=2824
  _globals['_DENOMOWNER']._serialized_start=2827
  _globals['_DENOMOWNER']._serialized_end=2955
  _globals['_QUERYDENOMOWNERSRESPONSE']._serialized_start=2958
  _globals['_QUERYDENOMOWNERSRESPONSE']._serialized_end=3125
  _globals['_QUERYDENOMOWNERSBYQUERYREQUEST']._serialized_start=3127
  _globals['_QUERYDENOMOWNERSBYQUERYREQUEST']._serialized_end=3253
  _globals['_QUERYDENOMOWNERSBYQUERYRESPONSE']._serialized_start=3256
  _globals['_QUERYDENOMOWNERSBYQUERYRESPONSE']._serialized_end=3430
  _globals['_QUERYSENDENABLEDREQUEST']._serialized_start=3432
  _globals['_QUERYSENDENABLEDREQUEST']._serialized_end=3553
  _globals['_QUERYSENDENABLEDRESPONSE']._serialized_start=3556
  _globals['_QUERYSENDENABLEDRESPONSE']._serialized_end=3724
  _globals['_QUERY']._serialized_start=3727
  _globals['_QUERY']._serialized_end=5977
# @@protoc_insertion_point(module_scope)
