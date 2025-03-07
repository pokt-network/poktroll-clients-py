"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import tendermint.crypto.keys_pb2
import tendermint.types.types_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Errors:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ErrorsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Errors.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ERRORS_UNKNOWN: _Errors.ValueType  # 0
    ERRORS_UNEXPECTED_RESPONSE: _Errors.ValueType  # 1
    ERRORS_NO_CONNECTION: _Errors.ValueType  # 2
    ERRORS_CONNECTION_TIMEOUT: _Errors.ValueType  # 3
    ERRORS_READ_TIMEOUT: _Errors.ValueType  # 4
    ERRORS_WRITE_TIMEOUT: _Errors.ValueType  # 5

class Errors(_Errors, metaclass=_ErrorsEnumTypeWrapper): ...

ERRORS_UNKNOWN: Errors.ValueType  # 0
ERRORS_UNEXPECTED_RESPONSE: Errors.ValueType  # 1
ERRORS_NO_CONNECTION: Errors.ValueType  # 2
ERRORS_CONNECTION_TIMEOUT: Errors.ValueType  # 3
ERRORS_READ_TIMEOUT: Errors.ValueType  # 4
ERRORS_WRITE_TIMEOUT: Errors.ValueType  # 5
global___Errors = Errors

@typing.final
class RemoteSignerError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    code: builtins.int
    description: builtins.str
    def __init__(
        self,
        *,
        code: builtins.int = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["code", b"code", "description", b"description"]) -> None: ...

global___RemoteSignerError = RemoteSignerError

@typing.final
class PubKeyRequest(google.protobuf.message.Message):
    """PubKeyRequest requests the consensus public key from the remote signer."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHAIN_ID_FIELD_NUMBER: builtins.int
    chain_id: builtins.str
    def __init__(
        self,
        *,
        chain_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["chain_id", b"chain_id"]) -> None: ...

global___PubKeyRequest = PubKeyRequest

@typing.final
class PubKeyResponse(google.protobuf.message.Message):
    """PubKeyResponse is a response message containing the public key."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUB_KEY_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def pub_key(self) -> tendermint.crypto.keys_pb2.PublicKey: ...
    @property
    def error(self) -> global___RemoteSignerError: ...
    def __init__(
        self,
        *,
        pub_key: tendermint.crypto.keys_pb2.PublicKey | None = ...,
        error: global___RemoteSignerError | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["error", b"error", "pub_key", b"pub_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["error", b"error", "pub_key", b"pub_key"]) -> None: ...

global___PubKeyResponse = PubKeyResponse

@typing.final
class SignVoteRequest(google.protobuf.message.Message):
    """SignVoteRequest is a request to sign a vote"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOTE_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    chain_id: builtins.str
    @property
    def vote(self) -> tendermint.types.types_pb2.Vote: ...
    def __init__(
        self,
        *,
        vote: tendermint.types.types_pb2.Vote | None = ...,
        chain_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["vote", b"vote"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["chain_id", b"chain_id", "vote", b"vote"]) -> None: ...

global___SignVoteRequest = SignVoteRequest

@typing.final
class SignedVoteResponse(google.protobuf.message.Message):
    """SignedVoteResponse is a response containing a signed vote or an error"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOTE_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def vote(self) -> tendermint.types.types_pb2.Vote: ...
    @property
    def error(self) -> global___RemoteSignerError: ...
    def __init__(
        self,
        *,
        vote: tendermint.types.types_pb2.Vote | None = ...,
        error: global___RemoteSignerError | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["error", b"error", "vote", b"vote"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["error", b"error", "vote", b"vote"]) -> None: ...

global___SignedVoteResponse = SignedVoteResponse

@typing.final
class SignProposalRequest(google.protobuf.message.Message):
    """SignProposalRequest is a request to sign a proposal"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    chain_id: builtins.str
    @property
    def proposal(self) -> tendermint.types.types_pb2.Proposal: ...
    def __init__(
        self,
        *,
        proposal: tendermint.types.types_pb2.Proposal | None = ...,
        chain_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["proposal", b"proposal"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["chain_id", b"chain_id", "proposal", b"proposal"]) -> None: ...

global___SignProposalRequest = SignProposalRequest

@typing.final
class SignedProposalResponse(google.protobuf.message.Message):
    """SignedProposalResponse is response containing a signed proposal or an error"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def proposal(self) -> tendermint.types.types_pb2.Proposal: ...
    @property
    def error(self) -> global___RemoteSignerError: ...
    def __init__(
        self,
        *,
        proposal: tendermint.types.types_pb2.Proposal | None = ...,
        error: global___RemoteSignerError | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["error", b"error", "proposal", b"proposal"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["error", b"error", "proposal", b"proposal"]) -> None: ...

global___SignedProposalResponse = SignedProposalResponse

@typing.final
class PingRequest(google.protobuf.message.Message):
    """PingRequest is a request to confirm that the connection is alive."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___PingRequest = PingRequest

@typing.final
class PingResponse(google.protobuf.message.Message):
    """PingResponse is a response to confirm that the connection is alive."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___PingResponse = PingResponse

@typing.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUB_KEY_REQUEST_FIELD_NUMBER: builtins.int
    PUB_KEY_RESPONSE_FIELD_NUMBER: builtins.int
    SIGN_VOTE_REQUEST_FIELD_NUMBER: builtins.int
    SIGNED_VOTE_RESPONSE_FIELD_NUMBER: builtins.int
    SIGN_PROPOSAL_REQUEST_FIELD_NUMBER: builtins.int
    SIGNED_PROPOSAL_RESPONSE_FIELD_NUMBER: builtins.int
    PING_REQUEST_FIELD_NUMBER: builtins.int
    PING_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def pub_key_request(self) -> global___PubKeyRequest: ...
    @property
    def pub_key_response(self) -> global___PubKeyResponse: ...
    @property
    def sign_vote_request(self) -> global___SignVoteRequest: ...
    @property
    def signed_vote_response(self) -> global___SignedVoteResponse: ...
    @property
    def sign_proposal_request(self) -> global___SignProposalRequest: ...
    @property
    def signed_proposal_response(self) -> global___SignedProposalResponse: ...
    @property
    def ping_request(self) -> global___PingRequest: ...
    @property
    def ping_response(self) -> global___PingResponse: ...
    def __init__(
        self,
        *,
        pub_key_request: global___PubKeyRequest | None = ...,
        pub_key_response: global___PubKeyResponse | None = ...,
        sign_vote_request: global___SignVoteRequest | None = ...,
        signed_vote_response: global___SignedVoteResponse | None = ...,
        sign_proposal_request: global___SignProposalRequest | None = ...,
        signed_proposal_response: global___SignedProposalResponse | None = ...,
        ping_request: global___PingRequest | None = ...,
        ping_response: global___PingResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ping_request", b"ping_request", "ping_response", b"ping_response", "pub_key_request", b"pub_key_request", "pub_key_response", b"pub_key_response", "sign_proposal_request", b"sign_proposal_request", "sign_vote_request", b"sign_vote_request", "signed_proposal_response", b"signed_proposal_response", "signed_vote_response", b"signed_vote_response", "sum", b"sum"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ping_request", b"ping_request", "ping_response", b"ping_response", "pub_key_request", b"pub_key_request", "pub_key_response", b"pub_key_response", "sign_proposal_request", b"sign_proposal_request", "sign_vote_request", b"sign_vote_request", "signed_proposal_response", b"signed_proposal_response", "signed_vote_response", b"signed_vote_response", "sum", b"sum"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["sum", b"sum"]) -> typing.Literal["pub_key_request", "pub_key_response", "sign_vote_request", "signed_vote_response", "sign_proposal_request", "signed_proposal_response", "ping_request", "ping_response"] | None: ...

global___Message = Message
