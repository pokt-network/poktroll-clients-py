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
import pocket.application.types_pb2
import pocket.migration.morse_onchain_pb2
import pocket.migration.params_pb2
import pocket.shared.service_pb2
import pocket.shared.supplier_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MsgUpdateParams(google.protobuf.message.Message):
    """MsgUpdateParams is the Msg/UpdateParams request type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    authority: builtins.str
    """authority is the address that controls the module (defaults to x/gov unless overwritten)."""
    @property
    def params(self) -> pocket.migration.params_pb2.Params:
        """params defines the module parameters to update.

        NOTE: All parameters must be supplied.
        """

    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        params: pocket.migration.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority", "params", b"params"]) -> None: ...

global___MsgUpdateParams = MsgUpdateParams

@typing.final
class MsgUpdateParamsResponse(google.protobuf.message.Message):
    """MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgUpdateParamsResponse = MsgUpdateParamsResponse

@typing.final
class MsgImportMorseClaimableAccounts(google.protobuf.message.Message):
    """MsgImportMorseClaimableAccounts is used to create the on-chain MorseClaimableAccounts ONLY AND EXACTLY ONCE (per network / re-genesis)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    MORSE_ACCOUNT_STATE_FIELD_NUMBER: builtins.int
    MORSE_ACCOUNT_STATE_HASH_FIELD_NUMBER: builtins.int
    authority: builtins.str
    """authority is the address that controls the module (defaults to x/gov unless overwritten)."""
    morse_account_state_hash: builtins.bytes
    """Verification can be done by comparing with locally derived Morse state like so:
      $ pocketd migrate collect-morse-accounts $<(pocket util export-genesis-for-reset)

    Additional documentation:
    - pocket util export-genesis-for-migration --help
    - pocketd migrate collect-morse-accounts --help
    """
    @property
    def morse_account_state(self) -> pocket.migration.morse_onchain_pb2.MorseAccountState:
        """the account state derived from the Morse state export and the `pocketd migrate collect-morse-accounts` command."""

    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        morse_account_state: pocket.migration.morse_onchain_pb2.MorseAccountState | None = ...,
        morse_account_state_hash: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["morse_account_state", b"morse_account_state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority", "morse_account_state", b"morse_account_state", "morse_account_state_hash", b"morse_account_state_hash"]) -> None: ...

global___MsgImportMorseClaimableAccounts = MsgImportMorseClaimableAccounts

@typing.final
class MsgImportMorseClaimableAccountsResponse(google.protobuf.message.Message):
    """MsgImportMorseClaimableAccountsResponse is returned from MsgImportMorseClaimableAccounts.
    It indicates the canonical hash of the imported MorseAccountState, and the number of claimable accounts which were imported.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATE_HASH_FIELD_NUMBER: builtins.int
    NUM_ACCOUNTS_FIELD_NUMBER: builtins.int
    state_hash: builtins.bytes
    """On-chain computed sha256 hash of the morse_account_state provided in the corresponding MsgCreateMorseAccountState."""
    num_accounts: builtins.int
    """Number of claimable accounts (EOAs) collected from Morse state export."""
    def __init__(
        self,
        *,
        state_hash: builtins.bytes = ...,
        num_accounts: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["num_accounts", b"num_accounts", "state_hash", b"state_hash"]) -> None: ...

global___MsgImportMorseClaimableAccountsResponse = MsgImportMorseClaimableAccountsResponse

@typing.final
class MsgClaimMorseAccount(google.protobuf.message.Message):
    """MsgClaimMorseAccount is used to execute a claim (one-time minting of tokens on Shannon),
    of the balance of the given Morse account, according to the on-chain MorseClaimableAccounts,
    to the balance of the given Shannon account.

    NOTE:
    - The Shannon account specified must be the message signer
    - Authz grants MAY be used to delegate claiming authority to other Shannon accounts
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHANNON_DEST_ADDRESS_FIELD_NUMBER: builtins.int
    MORSE_SRC_ADDRESS_FIELD_NUMBER: builtins.int
    MORSE_PUBLIC_KEY_FIELD_NUMBER: builtins.int
    MORSE_SIGNATURE_FIELD_NUMBER: builtins.int
    shannon_dest_address: builtins.str
    """The bech32-encoded address of the Shannon account to which the claimed balance will be minted."""
    morse_src_address: builtins.str
    """The hex-encoded address of the Morse account whose balance will be claimed.
    E.g.: 00f9900606fa3d5c9179fc0c8513078a53a2073e
    """
    morse_public_key: builtins.bytes
    """The ed25519 public key of the morse account with morse_src_address."""
    morse_signature: builtins.bytes
    """The hex-encoded signature, by the Morse account, of this message (where this field is nil).
    I.e.: morse_signature = private_key.sign(marshal(MsgClaimMorseAccount{morse_signature: nil, ...}))
    """
    def __init__(
        self,
        *,
        shannon_dest_address: builtins.str = ...,
        morse_src_address: builtins.str = ...,
        morse_public_key: builtins.bytes = ...,
        morse_signature: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["morse_public_key", b"morse_public_key", "morse_signature", b"morse_signature", "morse_src_address", b"morse_src_address", "shannon_dest_address", b"shannon_dest_address"]) -> None: ...

global___MsgClaimMorseAccount = MsgClaimMorseAccount

@typing.final
class MsgClaimMorseAccountResponse(google.protobuf.message.Message):
    """MsgClaimMorseAccountResponse is returned from MsgClaimMorseAccount.
    It indicates the morse_src_address of the account which was claimed, the total
    balance claimed, and the height at which the claim was committed.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MORSE_SRC_ADDRESS_FIELD_NUMBER: builtins.int
    CLAIMED_BALANCE_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    morse_src_address: builtins.str
    """The hex-encoded address of the Morse account whose balance will be claimed.
    E.g.: 00f9900606fa3d5c9179fc0c8513078a53a2073e
    """
    session_end_height: builtins.int
    """The session end height (on Shannon) in which the claim was committed (i.e. claimed)."""
    @property
    def claimed_balance(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """The balance which was claimed."""

    def __init__(
        self,
        *,
        morse_src_address: builtins.str = ...,
        claimed_balance: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        session_end_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["claimed_balance", b"claimed_balance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["claimed_balance", b"claimed_balance", "morse_src_address", b"morse_src_address", "session_end_height", b"session_end_height"]) -> None: ...

global___MsgClaimMorseAccountResponse = MsgClaimMorseAccountResponse

@typing.final
class MsgClaimMorseApplication(google.protobuf.message.Message):
    """MsgClaimMorseApplication is used to execute a claim (one-time minting of tokens on Shannon),
    of the total tokens owned by the given Morse account, according to the on-chain MorseClaimableAccounts,
    to the balance of the given Shannon account, followed by staking that Shannon account as an application
    for the given service_config and the same stake amount as on Morse.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHANNON_DEST_ADDRESS_FIELD_NUMBER: builtins.int
    MORSE_SRC_ADDRESS_FIELD_NUMBER: builtins.int
    MORSE_PUBLIC_KEY_FIELD_NUMBER: builtins.int
    MORSE_SIGNATURE_FIELD_NUMBER: builtins.int
    SERVICE_CONFIG_FIELD_NUMBER: builtins.int
    shannon_dest_address: builtins.str
    """The bech32-encoded address of the Shannon account to which the claimed tokens
    will be minted and from which the application will be staked.
    """
    morse_src_address: builtins.str
    """The hex-encoded address of the Morse account whose balance will be claimed.
    E.g.: 00f9900606fa3d5c9179fc0c8513078a53a2073e
    """
    morse_public_key: builtins.bytes
    """The ed25519 public key of the morse account with morse_src_address."""
    morse_signature: builtins.bytes
    """The hex-encoded signature, by the Morse account, of this message (where this field is nil).
    I.e.: morse_signature = private_key.sign(marshal(MsgClaimMorseAccount{morse_signature: nil, ...}))
    """
    @property
    def service_config(self) -> pocket.shared.service_pb2.ApplicationServiceConfig:
        """The services this application is staked to request service for.
        NOTE: This is not a repeated field, as in MsgStakeApplication,
        because an application can only be staked for one service.
        """

    def __init__(
        self,
        *,
        shannon_dest_address: builtins.str = ...,
        morse_src_address: builtins.str = ...,
        morse_public_key: builtins.bytes = ...,
        morse_signature: builtins.bytes = ...,
        service_config: pocket.shared.service_pb2.ApplicationServiceConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["service_config", b"service_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["morse_public_key", b"morse_public_key", "morse_signature", b"morse_signature", "morse_src_address", b"morse_src_address", "service_config", b"service_config", "shannon_dest_address", b"shannon_dest_address"]) -> None: ...

global___MsgClaimMorseApplication = MsgClaimMorseApplication

@typing.final
class MsgClaimMorseApplicationResponse(google.protobuf.message.Message):
    """MsgClaimMorseApplicationResponse is returned from MsgClaimMorseApplication.
    It indicates the morse_src_address of the account which was claimed, the unstaked
    balance claimed, the application stake, and the height at which the claim was committed.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MORSE_SRC_ADDRESS_FIELD_NUMBER: builtins.int
    CLAIMED_BALANCE_FIELD_NUMBER: builtins.int
    CLAIMEDAPPLICATIONSTAKE_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    APPLICATION_FIELD_NUMBER: builtins.int
    morse_src_address: builtins.str
    """The hex-encoded address of the Morse account whose balance will be claimed."""
    session_end_height: builtins.int
    """The session end height (on Shannon) in which the claim was committed (i.e. claimed)."""
    @property
    def claimed_balance(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """The unstaked balance which was claimed."""

    @property
    def claimedApplicationStake(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """The stake of the application which was staked as a result of the claim.
        If the application was already staked, this amount does not include the initial stake (i.e. only the portion which was "claimed").
        """

    @property
    def application(self) -> pocket.application.types_pb2.Application:
        """The application which was staked as a result of the claim."""

    def __init__(
        self,
        *,
        morse_src_address: builtins.str = ...,
        claimed_balance: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        claimedApplicationStake: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        session_end_height: builtins.int = ...,
        application: pocket.application.types_pb2.Application | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["application", b"application", "claimedApplicationStake", b"claimedApplicationStake", "claimed_balance", b"claimed_balance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["application", b"application", "claimedApplicationStake", b"claimedApplicationStake", "claimed_balance", b"claimed_balance", "morse_src_address", b"morse_src_address", "session_end_height", b"session_end_height"]) -> None: ...

global___MsgClaimMorseApplicationResponse = MsgClaimMorseApplicationResponse

@typing.final
class MsgClaimMorseSupplier(google.protobuf.message.Message):
    """MsgClaimMorseSupplier is used to:
    - Execute a one-time minting of tokens on Shannon based on tokens owned by the given Morse account
    - Use the on-chain MorseClaimableAccounts for verification
    - Credit the minted tokens to the balance of the given Shannon account
    - Automatically stake that Shannon account as a supplier

    NOTE: The supplier module's staking fee parameter (at the time of claiming) is deducted from the
    claimed balance.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHANNON_OWNER_ADDRESS_FIELD_NUMBER: builtins.int
    SHANNON_OPERATOR_ADDRESS_FIELD_NUMBER: builtins.int
    MORSE_PUBLIC_KEY_FIELD_NUMBER: builtins.int
    MORSE_SRC_ADDRESS_FIELD_NUMBER: builtins.int
    MORSE_SIGNATURE_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    shannon_owner_address: builtins.str
    """The bech32-encoded address of the Shannon account to which the claimed tokens
    will be minted and which become the supplier owner.
    See: https://dev.poktroll.com/operate/configs/supplier_staking_config#staking-types.
    """
    shannon_operator_address: builtins.str
    """The bech32-encoded address of the Shannon account to which will become the supplier operator.
    If empty, the shannon_owner_address will be used.
    See: https://dev.poktroll.com/operate/configs/supplier_staking_config#staking-types.
    """
    morse_public_key: builtins.bytes
    """The ed25519 public key of the morse account with morse_src_address."""
    morse_src_address: builtins.str
    """The hex-encoded address of the Morse account whose balance will be claimed.
    E.g.: 00f9900606fa3d5c9179fc0c8513078a53a2073e

    TODO_MAINNET(@bryanchriswhite, #1126): Rename to `morse_src_owner_address`.
    """
    morse_signature: builtins.bytes
    """The hex-encoded signature, by the Morse account, of this message (where this field is nil).
    I.e.: morse_signature = private_key.sign(marshal(MsgClaimMorseAccount{morse_signature: nil, ...}))

    TODO_MAINNET(@bryanchriswhite, #1126): Rename to `morse_src_owner_signature`.
    """
    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pocket.shared.service_pb2.SupplierServiceConfig]:
        """The services this supplier is staked to provide service for."""

    def __init__(
        self,
        *,
        shannon_owner_address: builtins.str = ...,
        shannon_operator_address: builtins.str = ...,
        morse_public_key: builtins.bytes = ...,
        morse_src_address: builtins.str = ...,
        morse_signature: builtins.bytes = ...,
        services: collections.abc.Iterable[pocket.shared.service_pb2.SupplierServiceConfig] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["morse_public_key", b"morse_public_key", "morse_signature", b"morse_signature", "morse_src_address", b"morse_src_address", "services", b"services", "shannon_operator_address", b"shannon_operator_address", "shannon_owner_address", b"shannon_owner_address"]) -> None: ...

global___MsgClaimMorseSupplier = MsgClaimMorseSupplier

@typing.final
class MsgClaimMorseSupplierResponse(google.protobuf.message.Message):
    """MsgClaimMorseSupplierResponse is returned from MsgClaimMorseSupplier.
    It indicates:
    - The morse_src_address of the claimed account
    - The unstaked balance claimed
    - The session end height in which the claim was committed
    - The staked supplier
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MORSE_SRC_ADDRESS_FIELD_NUMBER: builtins.int
    CLAIMED_BALANCE_FIELD_NUMBER: builtins.int
    CLAIMED_SUPPLIER_STAKE_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    SUPPLIER_FIELD_NUMBER: builtins.int
    morse_src_address: builtins.str
    """The hex-encoded address of the Morse account whose balance was claimed.
    E.g.: 00f9900606fa3d5c9179fc0c8513078a53a2073e
    """
    session_end_height: builtins.int
    """The session end height (on Shannon) in which the claim was committed (i.e. claimed)."""
    @property
    def claimed_balance(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """The unstaked balance which was claimed."""

    @property
    def claimed_supplier_stake(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    @property
    def supplier(self) -> pocket.shared.supplier_pb2.Supplier:
        """The supplier which was staked as a result of the claim."""

    def __init__(
        self,
        *,
        morse_src_address: builtins.str = ...,
        claimed_balance: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        claimed_supplier_stake: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        session_end_height: builtins.int = ...,
        supplier: pocket.shared.supplier_pb2.Supplier | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["claimed_balance", b"claimed_balance", "claimed_supplier_stake", b"claimed_supplier_stake", "supplier", b"supplier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["claimed_balance", b"claimed_balance", "claimed_supplier_stake", b"claimed_supplier_stake", "morse_src_address", b"morse_src_address", "session_end_height", b"session_end_height", "supplier", b"supplier"]) -> None: ...

global___MsgClaimMorseSupplierResponse = MsgClaimMorseSupplierResponse
