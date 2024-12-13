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
class Params(google.protobuf.message.Message):
    """Params defines the parameters for the module."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NUM_SUPPLIERS_PER_SESSION_FIELD_NUMBER: builtins.int
    num_suppliers_per_session: builtins.int
    """num_suppliers_per_session is the maximun number of suppliers per session
    (applicaiton:supplier pair for a given session number).
    """
    def __init__(
        self,
        *,
        num_suppliers_per_session: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["num_suppliers_per_session", b"num_suppliers_per_session"]) -> None: ...

global___Params = Params