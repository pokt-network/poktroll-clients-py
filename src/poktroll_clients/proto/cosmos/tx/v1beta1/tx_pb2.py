# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/tx/v1beta1/tx.proto
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
    'cosmos/tx/v1beta1/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from poktroll_clients.proto.amino import amino_pb2 as amino_dot_amino__pb2
from poktroll_clients.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from poktroll_clients.proto.cosmos.crypto.multisig.v1beta1 import multisig_pb2 as cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2
from poktroll_clients.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from poktroll_clients.proto.cosmos.tx.signing.v1beta1 import signing_pb2 as cosmos_dot_tx_dot_signing_dot_v1beta1_dot_signing__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from poktroll_clients.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63osmos/tx/v1beta1/tx.proto\x12\x11\x63osmos.tx.v1beta1\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a-cosmos/crypto/multisig/v1beta1/multisig.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\'cosmos/tx/signing/v1beta1/signing.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\x8d\x01\n\x02Tx\x12-\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x19.cosmos.tx.v1beta1.TxBodyR\x04\x62ody\x12\x38\n\tauth_info\x18\x02 \x01(\x0b\x32\x1b.cosmos.tx.v1beta1.AuthInfoR\x08\x61uthInfo\x12\x1e\n\nsignatures\x18\x03 \x03(\x0cR\nsignatures\"n\n\x05TxRaw\x12\x1d\n\nbody_bytes\x18\x01 \x01(\x0cR\tbodyBytes\x12&\n\x0f\x61uth_info_bytes\x18\x02 \x01(\x0cR\rauthInfoBytes\x12\x1e\n\nsignatures\x18\x03 \x03(\x0cR\nsignatures\"\x92\x01\n\x07SignDoc\x12\x1d\n\nbody_bytes\x18\x01 \x01(\x0cR\tbodyBytes\x12&\n\x0f\x61uth_info_bytes\x18\x02 \x01(\x0cR\rauthInfoBytes\x12\x19\n\x08\x63hain_id\x18\x03 \x01(\tR\x07\x63hainId\x12%\n\x0e\x61\x63\x63ount_number\x18\x04 \x01(\x04R\raccountNumber\"\xf2\x01\n\x10SignDocDirectAux\x12\x1d\n\nbody_bytes\x18\x01 \x01(\x0cR\tbodyBytes\x12\x33\n\npublic_key\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyR\tpublicKey\x12\x19\n\x08\x63hain_id\x18\x03 \x01(\tR\x07\x63hainId\x12%\n\x0e\x61\x63\x63ount_number\x18\x04 \x01(\x04R\raccountNumber\x12\x1a\n\x08sequence\x18\x05 \x01(\x04R\x08sequence\x12,\n\x03tip\x18\x06 \x01(\x0b\x32\x16.cosmos.tx.v1beta1.TipB\x02\x18\x01R\x03tip\"\xb3\x02\n\x06TxBody\x12\x30\n\x08messages\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyR\x08messages\x12\x12\n\x04memo\x18\x02 \x01(\tR\x04memo\x12%\n\x0etimeout_height\x18\x03 \x01(\x04R\rtimeoutHeight\x12\x1c\n\tunordered\x18\x04 \x01(\x08R\tunordered\x12\x42\n\x11\x65xtension_options\x18\xff\x07 \x03(\x0b\x32\x14.google.protobuf.AnyR\x10\x65xtensionOptions\x12Z\n\x1enon_critical_extension_options\x18\xff\x0f \x03(\x0b\x32\x14.google.protobuf.AnyR\x1bnonCriticalExtensionOptions\"\xa4\x01\n\x08\x41uthInfo\x12@\n\x0csigner_infos\x18\x01 \x03(\x0b\x32\x1d.cosmos.tx.v1beta1.SignerInfoR\x0bsignerInfos\x12(\n\x03\x66\x65\x65\x18\x02 \x01(\x0b\x32\x16.cosmos.tx.v1beta1.FeeR\x03\x66\x65\x65\x12,\n\x03tip\x18\x03 \x01(\x0b\x32\x16.cosmos.tx.v1beta1.TipB\x02\x18\x01R\x03tip\"\x97\x01\n\nSignerInfo\x12\x33\n\npublic_key\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\tpublicKey\x12\x38\n\tmode_info\x18\x02 \x01(\x0b\x32\x1b.cosmos.tx.v1beta1.ModeInfoR\x08modeInfo\x12\x1a\n\x08sequence\x18\x03 \x01(\x04R\x08sequence\"\xe0\x02\n\x08ModeInfo\x12<\n\x06single\x18\x01 \x01(\x0b\x32\".cosmos.tx.v1beta1.ModeInfo.SingleH\x00R\x06single\x12\x39\n\x05multi\x18\x02 \x01(\x0b\x32!.cosmos.tx.v1beta1.ModeInfo.MultiH\x00R\x05multi\x1a\x41\n\x06Single\x12\x37\n\x04mode\x18\x01 \x01(\x0e\x32#.cosmos.tx.signing.v1beta1.SignModeR\x04mode\x1a\x90\x01\n\x05Multi\x12K\n\x08\x62itarray\x18\x01 \x01(\x0b\x32/.cosmos.crypto.multisig.v1beta1.CompactBitArrayR\x08\x62itarray\x12:\n\nmode_infos\x18\x02 \x03(\x0b\x32\x1b.cosmos.tx.v1beta1.ModeInfoR\tmodeInfosB\x05\n\x03sum\"\x81\x02\n\x03\x46\x65\x65\x12y\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x06\x61mount\x12\x1b\n\tgas_limit\x18\x02 \x01(\x04R\x08gasLimit\x12.\n\x05payer\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05payer\x12\x32\n\x07granter\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07granter\"\xb6\x01\n\x03Tip\x12y\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x06\x61mount\x12\x30\n\x06tipper\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06tipper:\x02\x18\x01\"\xce\x01\n\rAuxSignerData\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12>\n\x08sign_doc\x18\x02 \x01(\x0b\x32#.cosmos.tx.v1beta1.SignDocDirectAuxR\x07signDoc\x12\x37\n\x04mode\x18\x03 \x01(\x0e\x32#.cosmos.tx.signing.v1beta1.SignModeR\x04mode\x12\x10\n\x03sig\x18\x04 \x01(\x0cR\x03sigB\'Z%github.com/cosmos/cosmos-sdk/types/txb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.tx.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/tx'
  _globals['_SIGNDOCDIRECTAUX'].fields_by_name['tip']._loaded_options = None
  _globals['_SIGNDOCDIRECTAUX'].fields_by_name['tip']._serialized_options = b'\030\001'
  _globals['_AUTHINFO'].fields_by_name['tip']._loaded_options = None
  _globals['_AUTHINFO'].fields_by_name['tip']._serialized_options = b'\030\001'
  _globals['_FEE'].fields_by_name['amount']._loaded_options = None
  _globals['_FEE'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_FEE'].fields_by_name['payer']._loaded_options = None
  _globals['_FEE'].fields_by_name['payer']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_FEE'].fields_by_name['granter']._loaded_options = None
  _globals['_FEE'].fields_by_name['granter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_TIP'].fields_by_name['amount']._loaded_options = None
  _globals['_TIP'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_TIP'].fields_by_name['tipper']._loaded_options = None
  _globals['_TIP'].fields_by_name['tipper']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_TIP']._loaded_options = None
  _globals['_TIP']._serialized_options = b'\030\001'
  _globals['_AUXSIGNERDATA'].fields_by_name['address']._loaded_options = None
  _globals['_AUXSIGNERDATA'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_TX']._serialized_start=265
  _globals['_TX']._serialized_end=406
  _globals['_TXRAW']._serialized_start=408
  _globals['_TXRAW']._serialized_end=518
  _globals['_SIGNDOC']._serialized_start=521
  _globals['_SIGNDOC']._serialized_end=667
  _globals['_SIGNDOCDIRECTAUX']._serialized_start=670
  _globals['_SIGNDOCDIRECTAUX']._serialized_end=912
  _globals['_TXBODY']._serialized_start=915
  _globals['_TXBODY']._serialized_end=1222
  _globals['_AUTHINFO']._serialized_start=1225
  _globals['_AUTHINFO']._serialized_end=1389
  _globals['_SIGNERINFO']._serialized_start=1392
  _globals['_SIGNERINFO']._serialized_end=1543
  _globals['_MODEINFO']._serialized_start=1546
  _globals['_MODEINFO']._serialized_end=1898
  _globals['_MODEINFO_SINGLE']._serialized_start=1679
  _globals['_MODEINFO_SINGLE']._serialized_end=1744
  _globals['_MODEINFO_MULTI']._serialized_start=1747
  _globals['_MODEINFO_MULTI']._serialized_end=1891
  _globals['_FEE']._serialized_start=1901
  _globals['_FEE']._serialized_end=2158
  _globals['_TIP']._serialized_start=2161
  _globals['_TIP']._serialized_end=2343
  _globals['_AUXSIGNERDATA']._serialized_start=2346
  _globals['_AUXSIGNERDATA']._serialized_end=2552
# @@protoc_insertion_point(module_scope)
