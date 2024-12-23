"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import tendermint.crypto.keys_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _BlockIDFlag:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _BlockIDFlagEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BlockIDFlag.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    BLOCK_ID_FLAG_UNKNOWN: _BlockIDFlag.ValueType  # 0
    """indicates an error condition"""
    BLOCK_ID_FLAG_ABSENT: _BlockIDFlag.ValueType  # 1
    """the vote was not received"""
    BLOCK_ID_FLAG_COMMIT: _BlockIDFlag.ValueType  # 2
    """voted for the block that received the majority"""
    BLOCK_ID_FLAG_NIL: _BlockIDFlag.ValueType  # 3
    """voted for nil"""

class BlockIDFlag(_BlockIDFlag, metaclass=_BlockIDFlagEnumTypeWrapper):
    """BlockIdFlag indicates which BlockID the signature is for"""

BLOCK_ID_FLAG_UNKNOWN: BlockIDFlag.ValueType  # 0
"""indicates an error condition"""
BLOCK_ID_FLAG_ABSENT: BlockIDFlag.ValueType  # 1
"""the vote was not received"""
BLOCK_ID_FLAG_COMMIT: BlockIDFlag.ValueType  # 2
"""voted for the block that received the majority"""
BLOCK_ID_FLAG_NIL: BlockIDFlag.ValueType  # 3
"""voted for nil"""
global___BlockIDFlag = BlockIDFlag

@typing.final
class ValidatorSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATORS_FIELD_NUMBER: builtins.int
    PROPOSER_FIELD_NUMBER: builtins.int
    TOTAL_VOTING_POWER_FIELD_NUMBER: builtins.int
    total_voting_power: builtins.int
    @property
    def validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Validator]: ...
    @property
    def proposer(self) -> global___Validator: ...
    def __init__(
        self,
        *,
        validators: collections.abc.Iterable[global___Validator] | None = ...,
        proposer: global___Validator | None = ...,
        total_voting_power: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["proposer", b"proposer"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["proposer", b"proposer", "total_voting_power", b"total_voting_power", "validators", b"validators"]) -> None: ...

global___ValidatorSet = ValidatorSet

@typing.final
class Validator(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    PUB_KEY_FIELD_NUMBER: builtins.int
    VOTING_POWER_FIELD_NUMBER: builtins.int
    PROPOSER_PRIORITY_FIELD_NUMBER: builtins.int
    address: builtins.bytes
    voting_power: builtins.int
    proposer_priority: builtins.int
    @property
    def pub_key(self) -> tendermint.crypto.keys_pb2.PublicKey: ...
    def __init__(
        self,
        *,
        address: builtins.bytes = ...,
        pub_key: tendermint.crypto.keys_pb2.PublicKey | None = ...,
        voting_power: builtins.int = ...,
        proposer_priority: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pub_key", b"pub_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "proposer_priority", b"proposer_priority", "pub_key", b"pub_key", "voting_power", b"voting_power"]) -> None: ...

global___Validator = Validator

@typing.final
class SimpleValidator(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUB_KEY_FIELD_NUMBER: builtins.int
    VOTING_POWER_FIELD_NUMBER: builtins.int
    voting_power: builtins.int
    @property
    def pub_key(self) -> tendermint.crypto.keys_pb2.PublicKey: ...
    def __init__(
        self,
        *,
        pub_key: tendermint.crypto.keys_pb2.PublicKey | None = ...,
        voting_power: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pub_key", b"pub_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pub_key", b"pub_key", "voting_power", b"voting_power"]) -> None: ...

global___SimpleValidator = SimpleValidator
