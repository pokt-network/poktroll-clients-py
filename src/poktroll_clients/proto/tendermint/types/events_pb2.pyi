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
class EventDataRoundState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    STEP_FIELD_NUMBER: builtins.int
    height: builtins.int
    round: builtins.int
    step: builtins.str
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        round: builtins.int = ...,
        step: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["height", b"height", "round", b"round", "step", b"step"]) -> None: ...

global___EventDataRoundState = EventDataRoundState