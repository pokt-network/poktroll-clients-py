"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import pocket.gateway.types_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class EventGatewayStaked(google.protobuf.message.Message):
    """EventGatewayStaked is emitted when a gateway is staked or up-staked."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GATEWAY_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    session_end_height: builtins.int
    """The end height of the session in which gateway was staked."""
    @property
    def gateway(self) -> pocket.gateway.types_pb2.Gateway:
        """The gateway that has been staked."""

    def __init__(
        self,
        *,
        gateway: pocket.gateway.types_pb2.Gateway | None = ...,
        session_end_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["gateway", b"gateway"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["gateway", b"gateway", "session_end_height", b"session_end_height"]) -> None: ...

global___EventGatewayStaked = EventGatewayStaked

@typing.final
class EventGatewayUnbondingBegin(google.protobuf.message.Message):
    """EventGatewayUnbondingBegin is emitted when a gateway begins unbonding.
    It is triggered by the commitment of an unstake gateway message.
    This event signals that a gateway has begun unbonding.
    The unbonding period is determined by the shared param gateway_unbonding_period_sessions.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GATEWAY_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    UNBONDING_END_HEIGHT_FIELD_NUMBER: builtins.int
    session_end_height: builtins.int
    """The end height of the session in which the unbonding began."""
    unbonding_end_height: builtins.int
    """The height at which gateway unbonding will end."""
    @property
    def gateway(self) -> pocket.gateway.types_pb2.Gateway: ...
    def __init__(
        self,
        *,
        gateway: pocket.gateway.types_pb2.Gateway | None = ...,
        session_end_height: builtins.int = ...,
        unbonding_end_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["gateway", b"gateway"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["gateway", b"gateway", "session_end_height", b"session_end_height", "unbonding_end_height", b"unbonding_end_height"]) -> None: ...

global___EventGatewayUnbondingBegin = EventGatewayUnbondingBegin

@typing.final
class EventGatewayUnbondingEnd(google.protobuf.message.Message):
    """EventGatewayUnbondingEnd is emitted when a gateway has completed unbonding.
    The unbonding period is determined by the shared param gateway_unbonding_period_sessions.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GATEWAY_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    UNBONDING_END_HEIGHT_FIELD_NUMBER: builtins.int
    session_end_height: builtins.int
    """The end height of the session in which the unbonding began."""
    unbonding_end_height: builtins.int
    """The height at which gateway unbonding will end."""
    @property
    def gateway(self) -> pocket.gateway.types_pb2.Gateway:
        """The gateway that has completed unbonding."""

    def __init__(
        self,
        *,
        gateway: pocket.gateway.types_pb2.Gateway | None = ...,
        session_end_height: builtins.int = ...,
        unbonding_end_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["gateway", b"gateway"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["gateway", b"gateway", "session_end_height", b"session_end_height", "unbonding_end_height", b"unbonding_end_height"]) -> None: ...

global___EventGatewayUnbondingEnd = EventGatewayUnbondingEnd

@typing.final
class EventGatewayUnbondingCanceled(google.protobuf.message.Message):
    """EventGatewayUnbondingCanceled is emitted when a gateway which was unbonding
    successfully (re-)stakes before the unbonding period has elapsed.
    An EventGatewayStaked event will also be emitted immediately after this event.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GATEWAY_FIELD_NUMBER: builtins.int
    SESSION_END_HEIGHT_FIELD_NUMBER: builtins.int
    session_end_height: builtins.int
    """The end height of the session in which the unbonding was canceled."""
    @property
    def gateway(self) -> pocket.gateway.types_pb2.Gateway: ...
    def __init__(
        self,
        *,
        gateway: pocket.gateway.types_pb2.Gateway | None = ...,
        session_end_height: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["gateway", b"gateway"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["gateway", b"gateway", "session_end_height", b"session_end_height"]) -> None: ...

global___EventGatewayUnbondingCanceled = EventGatewayUnbondingCanceled
