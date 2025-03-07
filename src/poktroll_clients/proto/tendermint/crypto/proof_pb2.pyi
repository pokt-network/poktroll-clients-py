"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Proof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOTAL_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    LEAF_HASH_FIELD_NUMBER: builtins.int
    AUNTS_FIELD_NUMBER: builtins.int
    total: builtins.int
    index: builtins.int
    leaf_hash: builtins.bytes
    @property
    def aunts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(
        self,
        *,
        total: builtins.int = ...,
        index: builtins.int = ...,
        leaf_hash: builtins.bytes = ...,
        aunts: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["aunts", b"aunts", "index", b"index", "leaf_hash", b"leaf_hash", "total", b"total"]) -> None: ...

global___Proof = Proof

@typing.final
class ValueOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    key: builtins.bytes
    """Encoded in ProofOp.Key."""
    @property
    def proof(self) -> global___Proof:
        """To encode in ProofOp.Data"""

    def __init__(
        self,
        *,
        key: builtins.bytes = ...,
        proof: global___Proof | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["proof", b"proof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "proof", b"proof"]) -> None: ...

global___ValueOp = ValueOp

@typing.final
class DominoOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    OUTPUT_FIELD_NUMBER: builtins.int
    key: builtins.str
    input: builtins.str
    output: builtins.str
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        input: builtins.str = ...,
        output: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["input", b"input", "key", b"key", "output", b"output"]) -> None: ...

global___DominoOp = DominoOp

@typing.final
class ProofOp(google.protobuf.message.Message):
    """ProofOp defines an operation used for calculating Merkle root
    The data could be arbitrary format, providing nessecary data
    for example neighbouring node hash
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    type: builtins.str
    key: builtins.bytes
    data: builtins.bytes
    def __init__(
        self,
        *,
        type: builtins.str = ...,
        key: builtins.bytes = ...,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data", b"data", "key", b"key", "type", b"type"]) -> None: ...

global___ProofOp = ProofOp

@typing.final
class ProofOps(google.protobuf.message.Message):
    """ProofOps is Merkle proof defined by the list of ProofOps"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPS_FIELD_NUMBER: builtins.int
    @property
    def ops(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProofOp]: ...
    def __init__(
        self,
        *,
        ops: collections.abc.Iterable[global___ProofOp] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ops", b"ops"]) -> None: ...

global___ProofOps = ProofOps
