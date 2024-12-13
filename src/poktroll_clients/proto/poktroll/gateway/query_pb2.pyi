"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import poktroll.gateway.params_pb2
import poktroll.gateway.types_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class QueryParamsRequest(google.protobuf.message.Message):
    """QueryParamsRequest is request type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

@typing.final
class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is response type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> poktroll.gateway.params_pb2.Params:
        """params holds all the parameters of this module."""

    def __init__(
        self,
        *,
        params: poktroll.gateway.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

@typing.final
class QueryGetGatewayRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address"]) -> None: ...

global___QueryGetGatewayRequest = QueryGetGatewayRequest

@typing.final
class QueryGetGatewayResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GATEWAY_FIELD_NUMBER: builtins.int
    @property
    def gateway(self) -> poktroll.gateway.types_pb2.Gateway: ...
    def __init__(
        self,
        *,
        gateway: poktroll.gateway.types_pb2.Gateway | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["gateway", b"gateway"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["gateway", b"gateway"]) -> None: ...

global___QueryGetGatewayResponse = QueryGetGatewayResponse

@typing.final
class QueryAllGatewaysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination"]) -> None: ...

global___QueryAllGatewaysRequest = QueryAllGatewaysRequest

@typing.final
class QueryAllGatewaysResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GATEWAYS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def gateways(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[poktroll.gateway.types_pb2.Gateway]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        gateways: collections.abc.Iterable[poktroll.gateway.types_pb2.Gateway] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["gateways", b"gateways", "pagination", b"pagination"]) -> None: ...

global___QueryAllGatewaysResponse = QueryAllGatewaysResponse