"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Module(google.protobuf.message.Message):
    """Module is the config object for the module."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    authority: builtins.str
    """authority defines the custom module authority. If not set, defaults to the governance module."""
    def __init__(
        self,
        *,
        authority: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority"]) -> None: ...

global___Module = Module
