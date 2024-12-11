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
import poktroll.application.params_pb2
import poktroll.application.types_pb2
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
    def params(self) -> poktroll.application.params_pb2.Params:
        """params holds all the parameters of this module."""

    def __init__(
        self,
        *,
        params: poktroll.application.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

@typing.final
class QueryGetApplicationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address"]) -> None: ...

global___QueryGetApplicationRequest = QueryGetApplicationRequest

@typing.final
class QueryGetApplicationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    APPLICATION_FIELD_NUMBER: builtins.int
    @property
    def application(self) -> poktroll.application.types_pb2.Application: ...
    def __init__(
        self,
        *,
        application: poktroll.application.types_pb2.Application | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["application", b"application"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["application", b"application"]) -> None: ...

global___QueryGetApplicationResponse = QueryGetApplicationResponse

@typing.final
class QueryAllApplicationsRequest(google.protobuf.message.Message):
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

global___QueryAllApplicationsRequest = QueryAllApplicationsRequest

@typing.final
class QueryAllApplicationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    APPLICATIONS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def applications(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[poktroll.application.types_pb2.Application]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        applications: collections.abc.Iterable[poktroll.application.types_pb2.Application] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["applications", b"applications", "pagination", b"pagination"]) -> None: ...

global___QueryAllApplicationsResponse = QueryAllApplicationsResponse
