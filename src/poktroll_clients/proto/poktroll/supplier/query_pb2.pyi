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
import poktroll.shared.supplier_pb2
import poktroll.supplier.params_pb2
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
    def params(self) -> poktroll.supplier.params_pb2.Params:
        """params holds all the parameters of this module."""

    def __init__(
        self,
        *,
        params: poktroll.supplier.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

@typing.final
class QueryGetSupplierRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATOR_ADDRESS_FIELD_NUMBER: builtins.int
    operator_address: builtins.str
    def __init__(
        self,
        *,
        operator_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["operator_address", b"operator_address"]) -> None: ...

global___QueryGetSupplierRequest = QueryGetSupplierRequest

@typing.final
class QueryGetSupplierResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPPLIER_FIELD_NUMBER: builtins.int
    @property
    def supplier(self) -> poktroll.shared.supplier_pb2.Supplier: ...
    def __init__(
        self,
        *,
        supplier: poktroll.shared.supplier_pb2.Supplier | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["supplier", b"supplier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["supplier", b"supplier"]) -> None: ...

global___QueryGetSupplierResponse = QueryGetSupplierResponse

@typing.final
class QueryAllSuppliersRequest(google.protobuf.message.Message):
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

global___QueryAllSuppliersRequest = QueryAllSuppliersRequest

@typing.final
class QueryAllSuppliersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPPLIER_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def supplier(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[poktroll.shared.supplier_pb2.Supplier]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        supplier: collections.abc.Iterable[poktroll.shared.supplier_pb2.Supplier] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["pagination", b"pagination", "supplier", b"supplier"]) -> None: ...

global___QueryAllSuppliersResponse = QueryAllSuppliersResponse
