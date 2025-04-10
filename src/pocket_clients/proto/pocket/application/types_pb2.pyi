"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
TODO_AUTOMATE: Add a CI workflow which detects .proto files with incompatible names (i.e. same as the package).
NB: This file CANNOT be named "application.proto" due to an as of yet unidentified
issue in how cosmos-proto generates the pulsar plugin output go source code.
"""

import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import pocket.shared.service_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Application(google.protobuf.message.Message):
    """Application represents the onchain definition and state of an application"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class PendingUndelegationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___UndelegatingGatewayList: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___UndelegatingGatewayList | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ADDRESS_FIELD_NUMBER: builtins.int
    STAKE_FIELD_NUMBER: builtins.int
    SERVICE_CONFIGS_FIELD_NUMBER: builtins.int
    DELEGATEE_GATEWAY_ADDRESSES_FIELD_NUMBER: builtins.int
    PENDING_UNDELEGATIONS_FIELD_NUMBER: builtins.int
    UNSTAKE_SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    PENDING_TRANSFER_FIELD_NUMBER: builtins.int
    address: builtins.str
    """Bech32 address of the application"""
    unstake_session_end_height: builtins.int
    """Session end height when application initiated unstaking (0 if not unstaking)"""
    @property
    def stake(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """Total amount of staked uPOKT"""

    @property
    def service_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pocket.shared.service_pb2.ApplicationServiceConfig]:
        """CRITICAL: Must contain EXACTLY ONE service config
        This prevents applications from over-servicing.
        Kept as repeated field for legacy and future compatibility
        Refs:
          - https://github.com/pokt-network/poktroll/pull/750#discussion_r1735025033
          - https://www.notion.so/buildwithgrove/Off-chain-Application-Stake-Tracking-6a8bebb107db4f7f9dc62cbe7ba555f7
        """

    @property
    def delegatee_gateway_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """TODO_MAINNET_MIGRATION(@bryanchriswhite): Rename `delegatee_gateway_addresses` to `gateway_addresses_delegated_to`.
        Ensure to rename all relevant configs, comments, variables, function names, etc as well.
        Non-nullable list of Bech32 encoded delegatee Gateway addresses
        """

    @property
    def pending_undelegations(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___UndelegatingGatewayList]:
        """Mapping of session end heights to gateways being undelegated from
        - Key: Height of the last block of the session when undelegation tx was committed
        - Value: List of gateways being undelegated from
        TODO_DOCUMENT(@red-0ne): Need to document the flow from this comment
        so its clear to everyone why this is necessary; https://github.com/pokt-network/poktroll/issues/476#issuecomment-2052639906.
        """

    @property
    def pending_transfer(self) -> global___PendingApplicationTransfer:
        """Information about pending application transfers"""

    def __init__(
        self,
        *,
        address: builtins.str = ...,
        stake: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        service_configs: collections.abc.Iterable[pocket.shared.service_pb2.ApplicationServiceConfig] | None = ...,
        delegatee_gateway_addresses: collections.abc.Iterable[builtins.str] | None = ...,
        pending_undelegations: collections.abc.Mapping[builtins.int, global___UndelegatingGatewayList] | None = ...,
        unstake_session_end_height: builtins.int = ...,
        pending_transfer: global___PendingApplicationTransfer | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pending_transfer", b"pending_transfer", "stake", b"stake"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "delegatee_gateway_addresses", b"delegatee_gateway_addresses", "pending_transfer", b"pending_transfer", "pending_undelegations", b"pending_undelegations", "service_configs", b"service_configs", "stake", b"stake", "unstake_session_end_height", b"unstake_session_end_height"]) -> None: ...

global___Application = Application

@typing.final
class UndelegatingGatewayList(google.protobuf.message.Message):
    """UndelegatingGatewayList is used as the Value of `pending_undelegations`.
    It is required to store a repeated list of strings as a map value.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GATEWAY_ADDRESSES_FIELD_NUMBER: builtins.int
    @property
    def gateway_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        gateway_addresses: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["gateway_addresses", b"gateway_addresses"]) -> None: ...

global___UndelegatingGatewayList = UndelegatingGatewayList

@typing.final
class PendingApplicationTransfer(google.protobuf.message.Message):
    """PendingTransfer is used to store the details of a pending transfer.
    It is only intended to be used inside of an Application object.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESTINATION_ADDRESS_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    destination_address: builtins.str
    session_end_height: builtins.int
    def __init__(
        self,
        *,
        destination_address: builtins.str = ...,
        session_end_height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["destination_address", b"destination_address", "session_end_height", b"session_end_height"]) -> None: ...

global___PendingApplicationTransfer = PendingApplicationTransfer
