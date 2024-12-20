"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import tendermint.abci.types_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class RequestPing(google.protobuf.message.Message):
    """----------------------------------------
    Request types
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RequestPing = RequestPing

@typing.final
class RequestBroadcastTx(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_FIELD_NUMBER: builtins.int
    tx: builtins.bytes
    def __init__(
        self,
        *,
        tx: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["tx", b"tx"]) -> None: ...

global___RequestBroadcastTx = RequestBroadcastTx

@typing.final
class ResponsePing(google.protobuf.message.Message):
    """----------------------------------------
    Response types
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ResponsePing = ResponsePing

@typing.final
class ResponseBroadcastTx(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHECK_TX_FIELD_NUMBER: builtins.int
    TX_RESULT_FIELD_NUMBER: builtins.int
    @property
    def check_tx(self) -> tendermint.abci.types_pb2.ResponseCheckTx: ...
    @property
    def tx_result(self) -> tendermint.abci.types_pb2.ExecTxResult: ...
    def __init__(
        self,
        *,
        check_tx: tendermint.abci.types_pb2.ResponseCheckTx | None = ...,
        tx_result: tendermint.abci.types_pb2.ExecTxResult | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["check_tx", b"check_tx", "tx_result", b"tx_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["check_tx", b"check_tx", "tx_result", b"tx_result"]) -> None: ...

global___ResponseBroadcastTx = ResponseBroadcastTx
