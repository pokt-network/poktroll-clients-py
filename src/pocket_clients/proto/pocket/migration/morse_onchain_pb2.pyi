"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MorseAccountState(google.protobuf.message.Message):
    """MorseAccountState is the onchain representation of all account state to be migrated from Morse.
    It is NEVER persisted onchain but is a dependency of the MsgImportMorseClaimableAccount handler.
    It's main purpose is to expose the #GetHash() method for verifying the integrity of all MorseClaimableAccounts.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MorseClaimableAccount]: ...
    def __init__(
        self,
        *,
        accounts: collections.abc.Iterable[global___MorseClaimableAccount] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["accounts", b"accounts"]) -> None: ...

global___MorseAccountState = MorseAccountState

@typing.final
class MorseClaimableAccount(google.protobuf.message.Message):
    """MorseClaimableAccount is the onchain (persisted) representation of a Morse
    account which is claimable as part of the Morse -> Shannon migration.
    They are intended to be created during MorseAccountState import (see: MsgImportMorseClaimableAccount).
    It is created ONLY ONCE and NEVER deleted (per morse_src_address per network / re-genesis).
    It is updated ONLY ONCE, when it is claimed (per morse_src_address per network / re-genesis).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHANNON_DEST_ADDRESS_FIELD_NUMBER: builtins.int
    MORSE_SRC_ADDRESS_FIELD_NUMBER: builtins.int
    UNSTAKED_BALANCE_FIELD_NUMBER: builtins.int
    SUPPLIER_STAKE_FIELD_NUMBER: builtins.int
    APPLICATION_STAKE_FIELD_NUMBER: builtins.int
    CLAIMED_AT_HEIGHT_FIELD_NUMBER: builtins.int
    shannon_dest_address: builtins.str
    """The bech32-encoded address of the Shannon account to which the claimed balance will be minted.
    This field is intended to remain empty until the account has been claimed.
    """
    morse_src_address: builtins.str
    """The hex-encoded address of the Morse account whose balance will be claimed."""
    claimed_at_height: builtins.int
    """The Shannon height at which the account was claimed.
    This field is intended to remain empty until the account has been claimed.
    """
    @property
    def unstaked_balance(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """The unstaked upokt tokens (i.e. account balance) available for claiming."""

    @property
    def supplier_stake(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """The staked tokens associated with a supplier actor which corresponds to this account address.
        DEV_NOTE: A few contextual notes related to Morse:
        - A Supplier is called a Servicer or Node (not a full node) in Morse
        - All Validators are Servicers, not all servicers are Validators
        - Automatically, the top 100 staked Servicers are validator
        - This only accounts for servicer stake balance transition
        TODO_MAINNET(@Olshansk): Develop a strategy for bootstrapping validators in Shannon by working with the cosmos ecosystem
        """

    @property
    def application_stake(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """The staked tokens associated with an application actor which corresponds to this account address."""

    def __init__(
        self,
        *,
        shannon_dest_address: builtins.str = ...,
        morse_src_address: builtins.str = ...,
        unstaked_balance: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        supplier_stake: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        application_stake: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        claimed_at_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["application_stake", b"application_stake", "supplier_stake", b"supplier_stake", "unstaked_balance", b"unstaked_balance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["application_stake", b"application_stake", "claimed_at_height", b"claimed_at_height", "morse_src_address", b"morse_src_address", "shannon_dest_address", b"shannon_dest_address", "supplier_stake", b"supplier_stake", "unstaked_balance", b"unstaked_balance"]) -> None: ...

global___MorseClaimableAccount = MorseClaimableAccount
