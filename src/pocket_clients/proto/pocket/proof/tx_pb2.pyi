"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.message
import pocket.proof.params_pb2
import pocket.proof.types_pb2
import pocket.session.types_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MsgUpdateParams(google.protobuf.message.Message):
    """MsgUpdateParams is the Msg/UpdateParams request type to update all params at once."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    authority: builtins.str
    """authority is the address that controls the module (defaults to x/gov unless overwritten)."""
    @property
    def params(self) -> pocket.proof.params_pb2.Params:
        """TODO_IMPROVE(#322): The requirement to provide all params is adopted from the
        latest Cosmos SDK version. We should look into either improving this ourselves
        or seeing if it is on their roadmap.

        params defines the x/proof parameters to update.
        NOTE: All parameters must be supplied.
        """

    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        params: pocket.proof.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authority", b"authority", "params", b"params"]) -> None: ...

global___MsgUpdateParams = MsgUpdateParams

@typing.final
class MsgUpdateParamsResponse(google.protobuf.message.Message):
    """MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgUpdateParamsResponse = MsgUpdateParamsResponse

@typing.final
class MsgUpdateParam(google.protobuf.message.Message):
    """MsgUpdateParam is the Msg/UpdateParam request type to update a single param."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    AS_BYTES_FIELD_NUMBER: builtins.int
    AS_FLOAT_FIELD_NUMBER: builtins.int
    AS_COIN_FIELD_NUMBER: builtins.int
    authority: builtins.str
    """authority is the address that controls the module (defaults to x/gov unless overwritten)."""
    name: builtins.str
    """The (name, as_type) tuple must match the corresponding name and type as
    specified in the `Params`` message in `proof/params.proto.`
    """
    as_bytes: builtins.bytes
    as_float: builtins.float
    @property
    def as_coin(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        name: builtins.str = ...,
        as_bytes: builtins.bytes = ...,
        as_float: builtins.float = ...,
        as_coin: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["as_bytes", b"as_bytes", "as_coin", b"as_coin", "as_float", b"as_float", "as_type", b"as_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["as_bytes", b"as_bytes", "as_coin", b"as_coin", "as_float", b"as_float", "as_type", b"as_type", "authority", b"authority", "name", b"name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["as_type", b"as_type"]) -> typing.Literal["as_bytes", "as_float", "as_coin"] | None: ...

global___MsgUpdateParam = MsgUpdateParam

@typing.final
class MsgUpdateParamResponse(google.protobuf.message.Message):
    """MsgUpdateParamResponse defines the response structure for executing a
    MsgUpdateParam message after a single param update.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> pocket.proof.params_pb2.Params: ...
    def __init__(
        self,
        *,
        params: pocket.proof.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params"]) -> None: ...

global___MsgUpdateParamResponse = MsgUpdateParamResponse

@typing.final
class MsgCreateClaim(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPPLIER_OPERATOR_ADDRESS_FIELD_NUMBER: builtins.int
    SESSION_HEADER_FIELD_NUMBER: builtins.int
    ROOT_HASH_FIELD_NUMBER: builtins.int
    supplier_operator_address: builtins.str
    root_hash: builtins.bytes
    """root returned from smt.SMST#Root()"""
    @property
    def session_header(self) -> pocket.session.types_pb2.SessionHeader: ...
    def __init__(
        self,
        *,
        supplier_operator_address: builtins.str = ...,
        session_header: pocket.session.types_pb2.SessionHeader | None = ...,
        root_hash: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["session_header", b"session_header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["root_hash", b"root_hash", "session_header", b"session_header", "supplier_operator_address", b"supplier_operator_address"]) -> None: ...

global___MsgCreateClaim = MsgCreateClaim

@typing.final
class MsgCreateClaimResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLAIM_FIELD_NUMBER: builtins.int
    @property
    def claim(self) -> pocket.proof.types_pb2.Claim: ...
    def __init__(
        self,
        *,
        claim: pocket.proof.types_pb2.Claim | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["claim", b"claim"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["claim", b"claim"]) -> None: ...

global___MsgCreateClaimResponse = MsgCreateClaimResponse

@typing.final
class MsgSubmitProof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPPLIER_OPERATOR_ADDRESS_FIELD_NUMBER: builtins.int
    SESSION_HEADER_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    supplier_operator_address: builtins.str
    proof: builtins.bytes
    """serialized version of *smt.SparseCompactMerkleClosestProof"""
    @property
    def session_header(self) -> pocket.session.types_pb2.SessionHeader: ...
    def __init__(
        self,
        *,
        supplier_operator_address: builtins.str = ...,
        session_header: pocket.session.types_pb2.SessionHeader | None = ...,
        proof: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["session_header", b"session_header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["proof", b"proof", "session_header", b"session_header", "supplier_operator_address", b"supplier_operator_address"]) -> None: ...

global___MsgSubmitProof = MsgSubmitProof

@typing.final
class MsgSubmitProofResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROOF_FIELD_NUMBER: builtins.int
    @property
    def proof(self) -> pocket.proof.types_pb2.Proof: ...
    def __init__(
        self,
        *,
        proof: pocket.proof.types_pb2.Proof | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["proof", b"proof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["proof", b"proof"]) -> None: ...

global___MsgSubmitProofResponse = MsgSubmitProofResponse
