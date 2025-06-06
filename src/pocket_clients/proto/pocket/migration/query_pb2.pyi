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
import pocket.migration.morse_onchain_pb2
import pocket.migration.params_pb2
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
    def params(self) -> pocket.migration.params_pb2.Params:
        """params holds all the parameters of this module."""

    def __init__(
        self,
        *,
        params: pocket.migration.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

@typing.final
class QueryMorseClaimableAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address"]) -> None: ...

global___QueryMorseClaimableAccountRequest = QueryMorseClaimableAccountRequest

@typing.final
class QueryMorseClaimableAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MORSECLAIMABLEACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def morseClaimableAccount(self) -> pocket.migration.morse_onchain_pb2.MorseClaimableAccount: ...
    def __init__(
        self,
        *,
        morseClaimableAccount: pocket.migration.morse_onchain_pb2.MorseClaimableAccount | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["morseClaimableAccount", b"morseClaimableAccount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["morseClaimableAccount", b"morseClaimableAccount"]) -> None: ...

global___QueryMorseClaimableAccountResponse = QueryMorseClaimableAccountResponse

@typing.final
class QueryAllMorseClaimableAccountRequest(google.protobuf.message.Message):
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

global___QueryAllMorseClaimableAccountRequest = QueryAllMorseClaimableAccountRequest

@typing.final
class QueryAllMorseClaimableAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MORSECLAIMABLEACCOUNT_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def morseClaimableAccount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pocket.migration.morse_onchain_pb2.MorseClaimableAccount]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        morseClaimableAccount: collections.abc.Iterable[pocket.migration.morse_onchain_pb2.MorseClaimableAccount] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["morseClaimableAccount", b"morseClaimableAccount", "pagination", b"pagination"]) -> None: ...

global___QueryAllMorseClaimableAccountResponse = QueryAllMorseClaimableAccountResponse
