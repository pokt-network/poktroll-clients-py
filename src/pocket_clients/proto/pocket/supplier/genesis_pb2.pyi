"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import pocket.shared.supplier_pb2
import pocket.supplier.params_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the supplier module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    SUPPLIERLIST_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> pocket.supplier.params_pb2.Params:
        """params defines all the parameters of the module."""

    @property
    def supplierList(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pocket.shared.supplier_pb2.Supplier]: ...
    def __init__(
        self,
        *,
        params: pocket.supplier.params_pb2.Params | None = ...,
        supplierList: collections.abc.Iterable[pocket.shared.supplier_pb2.Supplier] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params", "supplierList", b"supplierList"]) -> None: ...

global___GenesisState = GenesisState
