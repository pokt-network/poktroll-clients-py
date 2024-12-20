"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import tendermint.libs.bits.types_pb2
import tendermint.types.types_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class NewRoundStep(google.protobuf.message.Message):
    """NewRoundStep is sent for every step taken in the ConsensusState.
    For every height/round/step transition
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    STEP_FIELD_NUMBER: builtins.int
    SECONDS_SINCE_START_TIME_FIELD_NUMBER: builtins.int
    LAST_COMMIT_ROUND_FIELD_NUMBER: builtins.int
    height: builtins.int
    round: builtins.int
    step: builtins.int
    seconds_since_start_time: builtins.int
    last_commit_round: builtins.int
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        round: builtins.int = ...,
        step: builtins.int = ...,
        seconds_since_start_time: builtins.int = ...,
        last_commit_round: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["height", b"height", "last_commit_round", b"last_commit_round", "round", b"round", "seconds_since_start_time", b"seconds_since_start_time", "step", b"step"]) -> None: ...

global___NewRoundStep = NewRoundStep

@typing.final
class NewValidBlock(google.protobuf.message.Message):
    """NewValidBlock is sent when a validator observes a valid block B in some round r,
    i.e., there is a Proposal for block B and 2/3+ prevotes for the block B in the round r.
    In case the block is also committed, then IsCommit flag is set to true.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    BLOCK_PART_SET_HEADER_FIELD_NUMBER: builtins.int
    BLOCK_PARTS_FIELD_NUMBER: builtins.int
    IS_COMMIT_FIELD_NUMBER: builtins.int
    height: builtins.int
    round: builtins.int
    is_commit: builtins.bool
    @property
    def block_part_set_header(self) -> tendermint.types.types_pb2.PartSetHeader: ...
    @property
    def block_parts(self) -> tendermint.libs.bits.types_pb2.BitArray: ...
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        round: builtins.int = ...,
        block_part_set_header: tendermint.types.types_pb2.PartSetHeader | None = ...,
        block_parts: tendermint.libs.bits.types_pb2.BitArray | None = ...,
        is_commit: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["block_part_set_header", b"block_part_set_header", "block_parts", b"block_parts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["block_part_set_header", b"block_part_set_header", "block_parts", b"block_parts", "height", b"height", "is_commit", b"is_commit", "round", b"round"]) -> None: ...

global___NewValidBlock = NewValidBlock

@typing.final
class Proposal(google.protobuf.message.Message):
    """Proposal is sent when a new block is proposed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_FIELD_NUMBER: builtins.int
    @property
    def proposal(self) -> tendermint.types.types_pb2.Proposal: ...
    def __init__(
        self,
        *,
        proposal: tendermint.types.types_pb2.Proposal | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["proposal", b"proposal"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["proposal", b"proposal"]) -> None: ...

global___Proposal = Proposal

@typing.final
class ProposalPOL(google.protobuf.message.Message):
    """ProposalPOL is sent when a previous proposal is re-proposed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    PROPOSAL_POL_ROUND_FIELD_NUMBER: builtins.int
    PROPOSAL_POL_FIELD_NUMBER: builtins.int
    height: builtins.int
    proposal_pol_round: builtins.int
    @property
    def proposal_pol(self) -> tendermint.libs.bits.types_pb2.BitArray: ...
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        proposal_pol_round: builtins.int = ...,
        proposal_pol: tendermint.libs.bits.types_pb2.BitArray | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["proposal_pol", b"proposal_pol"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["height", b"height", "proposal_pol", b"proposal_pol", "proposal_pol_round", b"proposal_pol_round"]) -> None: ...

global___ProposalPOL = ProposalPOL

@typing.final
class BlockPart(google.protobuf.message.Message):
    """BlockPart is sent when gossipping a piece of the proposed block."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    PART_FIELD_NUMBER: builtins.int
    height: builtins.int
    round: builtins.int
    @property
    def part(self) -> tendermint.types.types_pb2.Part: ...
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        round: builtins.int = ...,
        part: tendermint.types.types_pb2.Part | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["part", b"part"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["height", b"height", "part", b"part", "round", b"round"]) -> None: ...

global___BlockPart = BlockPart

@typing.final
class Vote(google.protobuf.message.Message):
    """Vote is sent when voting for a proposal (or lack thereof)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOTE_FIELD_NUMBER: builtins.int
    @property
    def vote(self) -> tendermint.types.types_pb2.Vote: ...
    def __init__(
        self,
        *,
        vote: tendermint.types.types_pb2.Vote | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["vote", b"vote"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["vote", b"vote"]) -> None: ...

global___Vote = Vote

@typing.final
class HasVote(google.protobuf.message.Message):
    """HasVote is sent to indicate that a particular vote has been received."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    height: builtins.int
    round: builtins.int
    type: tendermint.types.types_pb2.SignedMsgType.ValueType
    index: builtins.int
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        round: builtins.int = ...,
        type: tendermint.types.types_pb2.SignedMsgType.ValueType = ...,
        index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["height", b"height", "index", b"index", "round", b"round", "type", b"type"]) -> None: ...

global___HasVote = HasVote

@typing.final
class VoteSetMaj23(google.protobuf.message.Message):
    """VoteSetMaj23 is sent to indicate that a given BlockID has seen +2/3 votes."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    BLOCK_ID_FIELD_NUMBER: builtins.int
    height: builtins.int
    round: builtins.int
    type: tendermint.types.types_pb2.SignedMsgType.ValueType
    @property
    def block_id(self) -> tendermint.types.types_pb2.BlockID: ...
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        round: builtins.int = ...,
        type: tendermint.types.types_pb2.SignedMsgType.ValueType = ...,
        block_id: tendermint.types.types_pb2.BlockID | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["block_id", b"block_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["block_id", b"block_id", "height", b"height", "round", b"round", "type", b"type"]) -> None: ...

global___VoteSetMaj23 = VoteSetMaj23

@typing.final
class VoteSetBits(google.protobuf.message.Message):
    """VoteSetBits is sent to communicate the bit-array of votes seen for the BlockID."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    BLOCK_ID_FIELD_NUMBER: builtins.int
    VOTES_FIELD_NUMBER: builtins.int
    height: builtins.int
    round: builtins.int
    type: tendermint.types.types_pb2.SignedMsgType.ValueType
    @property
    def block_id(self) -> tendermint.types.types_pb2.BlockID: ...
    @property
    def votes(self) -> tendermint.libs.bits.types_pb2.BitArray: ...
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        round: builtins.int = ...,
        type: tendermint.types.types_pb2.SignedMsgType.ValueType = ...,
        block_id: tendermint.types.types_pb2.BlockID | None = ...,
        votes: tendermint.libs.bits.types_pb2.BitArray | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["block_id", b"block_id", "votes", b"votes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["block_id", b"block_id", "height", b"height", "round", b"round", "type", b"type", "votes", b"votes"]) -> None: ...

global___VoteSetBits = VoteSetBits

@typing.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEW_ROUND_STEP_FIELD_NUMBER: builtins.int
    NEW_VALID_BLOCK_FIELD_NUMBER: builtins.int
    PROPOSAL_FIELD_NUMBER: builtins.int
    PROPOSAL_POL_FIELD_NUMBER: builtins.int
    BLOCK_PART_FIELD_NUMBER: builtins.int
    VOTE_FIELD_NUMBER: builtins.int
    HAS_VOTE_FIELD_NUMBER: builtins.int
    VOTE_SET_MAJ23_FIELD_NUMBER: builtins.int
    VOTE_SET_BITS_FIELD_NUMBER: builtins.int
    @property
    def new_round_step(self) -> global___NewRoundStep: ...
    @property
    def new_valid_block(self) -> global___NewValidBlock: ...
    @property
    def proposal(self) -> global___Proposal: ...
    @property
    def proposal_pol(self) -> global___ProposalPOL: ...
    @property
    def block_part(self) -> global___BlockPart: ...
    @property
    def vote(self) -> global___Vote: ...
    @property
    def has_vote(self) -> global___HasVote: ...
    @property
    def vote_set_maj23(self) -> global___VoteSetMaj23: ...
    @property
    def vote_set_bits(self) -> global___VoteSetBits: ...
    def __init__(
        self,
        *,
        new_round_step: global___NewRoundStep | None = ...,
        new_valid_block: global___NewValidBlock | None = ...,
        proposal: global___Proposal | None = ...,
        proposal_pol: global___ProposalPOL | None = ...,
        block_part: global___BlockPart | None = ...,
        vote: global___Vote | None = ...,
        has_vote: global___HasVote | None = ...,
        vote_set_maj23: global___VoteSetMaj23 | None = ...,
        vote_set_bits: global___VoteSetBits | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["block_part", b"block_part", "has_vote", b"has_vote", "new_round_step", b"new_round_step", "new_valid_block", b"new_valid_block", "proposal", b"proposal", "proposal_pol", b"proposal_pol", "sum", b"sum", "vote", b"vote", "vote_set_bits", b"vote_set_bits", "vote_set_maj23", b"vote_set_maj23"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["block_part", b"block_part", "has_vote", b"has_vote", "new_round_step", b"new_round_step", "new_valid_block", b"new_valid_block", "proposal", b"proposal", "proposal_pol", b"proposal_pol", "sum", b"sum", "vote", b"vote", "vote_set_bits", b"vote_set_bits", "vote_set_maj23", b"vote_set_maj23"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["sum", b"sum"]) -> typing.Literal["new_round_step", "new_valid_block", "proposal", "proposal_pol", "block_part", "vote", "has_vote", "vote_set_maj23", "vote_set_bits"] | None: ...

global___Message = Message
