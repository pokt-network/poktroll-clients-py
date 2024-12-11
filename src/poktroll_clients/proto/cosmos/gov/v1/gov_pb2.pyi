"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.46"""

import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ProposalType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ProposalTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProposalType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PROPOSAL_TYPE_UNSPECIFIED: _ProposalType.ValueType  # 0
    """PROPOSAL_TYPE_UNSPECIFIED defines no proposal type, which fallback to PROPOSAL_TYPE_STANDARD."""
    PROPOSAL_TYPE_STANDARD: _ProposalType.ValueType  # 1
    """PROPOSAL_TYPE_STANDARD defines the type for a standard proposal."""
    PROPOSAL_TYPE_MULTIPLE_CHOICE: _ProposalType.ValueType  # 2
    """PROPOSAL_TYPE_MULTIPLE_CHOICE defines the type for a multiple choice proposal."""
    PROPOSAL_TYPE_OPTIMISTIC: _ProposalType.ValueType  # 3
    """PROPOSAL_TYPE_OPTIMISTIC defines the type for an optimistic proposal."""
    PROPOSAL_TYPE_EXPEDITED: _ProposalType.ValueType  # 4
    """PROPOSAL_TYPE_EXPEDITED defines the type for an expedited proposal."""

class ProposalType(_ProposalType, metaclass=_ProposalTypeEnumTypeWrapper):
    """ProposalType enumerates the valid proposal types.
    All proposal types are v1.Proposal which have different voting periods or tallying logic.
    """

PROPOSAL_TYPE_UNSPECIFIED: ProposalType.ValueType  # 0
"""PROPOSAL_TYPE_UNSPECIFIED defines no proposal type, which fallback to PROPOSAL_TYPE_STANDARD."""
PROPOSAL_TYPE_STANDARD: ProposalType.ValueType  # 1
"""PROPOSAL_TYPE_STANDARD defines the type for a standard proposal."""
PROPOSAL_TYPE_MULTIPLE_CHOICE: ProposalType.ValueType  # 2
"""PROPOSAL_TYPE_MULTIPLE_CHOICE defines the type for a multiple choice proposal."""
PROPOSAL_TYPE_OPTIMISTIC: ProposalType.ValueType  # 3
"""PROPOSAL_TYPE_OPTIMISTIC defines the type for an optimistic proposal."""
PROPOSAL_TYPE_EXPEDITED: ProposalType.ValueType  # 4
"""PROPOSAL_TYPE_EXPEDITED defines the type for an expedited proposal."""
global___ProposalType = ProposalType

class _VoteOption:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VoteOptionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VoteOption.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VOTE_OPTION_UNSPECIFIED: _VoteOption.ValueType  # 0
    """VOTE_OPTION_UNSPECIFIED defines a no-op vote option."""
    VOTE_OPTION_ONE: _VoteOption.ValueType  # 1
    """VOTE_OPTION_ONE defines the first proposal vote option."""
    VOTE_OPTION_YES: _VoteOption.ValueType  # 1
    """VOTE_OPTION_YES defines the yes proposal vote option."""
    VOTE_OPTION_TWO: _VoteOption.ValueType  # 2
    """VOTE_OPTION_TWO defines the second proposal vote option."""
    VOTE_OPTION_ABSTAIN: _VoteOption.ValueType  # 2
    """VOTE_OPTION_ABSTAIN defines the abstain proposal vote option."""
    VOTE_OPTION_THREE: _VoteOption.ValueType  # 3
    """VOTE_OPTION_THREE defines the third proposal vote option."""
    VOTE_OPTION_NO: _VoteOption.ValueType  # 3
    """VOTE_OPTION_NO defines the no proposal vote option."""
    VOTE_OPTION_FOUR: _VoteOption.ValueType  # 4
    """VOTE_OPTION_FOUR defines the fourth proposal vote option."""
    VOTE_OPTION_NO_WITH_VETO: _VoteOption.ValueType  # 4
    """VOTE_OPTION_NO_WITH_VETO defines the no with veto proposal vote option."""
    VOTE_OPTION_SPAM: _VoteOption.ValueType  # 5
    """VOTE_OPTION_SPAM defines the spam proposal vote option."""

class VoteOption(_VoteOption, metaclass=_VoteOptionEnumTypeWrapper):
    """VoteOption enumerates the valid vote options for a given governance proposal."""

VOTE_OPTION_UNSPECIFIED: VoteOption.ValueType  # 0
"""VOTE_OPTION_UNSPECIFIED defines a no-op vote option."""
VOTE_OPTION_ONE: VoteOption.ValueType  # 1
"""VOTE_OPTION_ONE defines the first proposal vote option."""
VOTE_OPTION_YES: VoteOption.ValueType  # 1
"""VOTE_OPTION_YES defines the yes proposal vote option."""
VOTE_OPTION_TWO: VoteOption.ValueType  # 2
"""VOTE_OPTION_TWO defines the second proposal vote option."""
VOTE_OPTION_ABSTAIN: VoteOption.ValueType  # 2
"""VOTE_OPTION_ABSTAIN defines the abstain proposal vote option."""
VOTE_OPTION_THREE: VoteOption.ValueType  # 3
"""VOTE_OPTION_THREE defines the third proposal vote option."""
VOTE_OPTION_NO: VoteOption.ValueType  # 3
"""VOTE_OPTION_NO defines the no proposal vote option."""
VOTE_OPTION_FOUR: VoteOption.ValueType  # 4
"""VOTE_OPTION_FOUR defines the fourth proposal vote option."""
VOTE_OPTION_NO_WITH_VETO: VoteOption.ValueType  # 4
"""VOTE_OPTION_NO_WITH_VETO defines the no with veto proposal vote option."""
VOTE_OPTION_SPAM: VoteOption.ValueType  # 5
"""VOTE_OPTION_SPAM defines the spam proposal vote option."""
global___VoteOption = VoteOption

class _ProposalStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ProposalStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProposalStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PROPOSAL_STATUS_UNSPECIFIED: _ProposalStatus.ValueType  # 0
    """PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status."""
    PROPOSAL_STATUS_DEPOSIT_PERIOD: _ProposalStatus.ValueType  # 1
    """PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit
    period.
    """
    PROPOSAL_STATUS_VOTING_PERIOD: _ProposalStatus.ValueType  # 2
    """PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting
    period.
    """
    PROPOSAL_STATUS_PASSED: _ProposalStatus.ValueType  # 3
    """PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has
    passed.
    """
    PROPOSAL_STATUS_REJECTED: _ProposalStatus.ValueType  # 4
    """PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has
    been rejected.
    """
    PROPOSAL_STATUS_FAILED: _ProposalStatus.ValueType  # 5
    """PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has
    failed.
    """

class ProposalStatus(_ProposalStatus, metaclass=_ProposalStatusEnumTypeWrapper):
    """ProposalStatus enumerates the valid statuses of a proposal."""

PROPOSAL_STATUS_UNSPECIFIED: ProposalStatus.ValueType  # 0
"""PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status."""
PROPOSAL_STATUS_DEPOSIT_PERIOD: ProposalStatus.ValueType  # 1
"""PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit
period.
"""
PROPOSAL_STATUS_VOTING_PERIOD: ProposalStatus.ValueType  # 2
"""PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting
period.
"""
PROPOSAL_STATUS_PASSED: ProposalStatus.ValueType  # 3
"""PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has
passed.
"""
PROPOSAL_STATUS_REJECTED: ProposalStatus.ValueType  # 4
"""PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has
been rejected.
"""
PROPOSAL_STATUS_FAILED: ProposalStatus.ValueType  # 5
"""PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has
failed.
"""
global___ProposalStatus = ProposalStatus

@typing.final
class WeightedVoteOption(google.protobuf.message.Message):
    """WeightedVoteOption defines a unit of vote for vote split."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPTION_FIELD_NUMBER: builtins.int
    WEIGHT_FIELD_NUMBER: builtins.int
    option: global___VoteOption.ValueType
    """option defines the valid vote options, it must not contain duplicate vote options."""
    weight: builtins.str
    """weight is the vote weight associated with the vote option."""
    def __init__(
        self,
        *,
        option: global___VoteOption.ValueType = ...,
        weight: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["option", b"option", "weight", b"weight"]) -> None: ...

global___WeightedVoteOption = WeightedVoteOption

@typing.final
class Deposit(google.protobuf.message.Message):
    """Deposit defines an amount deposited by an account address to an active
    proposal.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    DEPOSITOR_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    depositor: builtins.str
    """depositor defines the deposit addresses from the proposals."""
    @property
    def amount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """amount to be deposited by depositor."""

    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        depositor: builtins.str = ...,
        amount: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["amount", b"amount", "depositor", b"depositor", "proposal_id", b"proposal_id"]) -> None: ...

global___Deposit = Deposit

@typing.final
class Proposal(google.protobuf.message.Message):
    """Proposal defines the core field members of a governance proposal."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    MESSAGES_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    FINAL_TALLY_RESULT_FIELD_NUMBER: builtins.int
    SUBMIT_TIME_FIELD_NUMBER: builtins.int
    DEPOSIT_END_TIME_FIELD_NUMBER: builtins.int
    TOTAL_DEPOSIT_FIELD_NUMBER: builtins.int
    VOTING_START_TIME_FIELD_NUMBER: builtins.int
    VOTING_END_TIME_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    PROPOSER_FIELD_NUMBER: builtins.int
    EXPEDITED_FIELD_NUMBER: builtins.int
    FAILED_REASON_FIELD_NUMBER: builtins.int
    PROPOSAL_TYPE_FIELD_NUMBER: builtins.int
    id: builtins.int
    """id defines the unique id of the proposal."""
    status: global___ProposalStatus.ValueType
    """status defines the proposal status."""
    metadata: builtins.str
    """metadata is any arbitrary metadata attached to the proposal.
    the recommended format of the metadata is to be found here:
    https://docs.cosmos.network/v0.47/modules/gov#proposal-3
    """
    title: builtins.str
    """title is the title of the proposal

    Since: cosmos-sdk 0.47
    """
    summary: builtins.str
    """summary is a short summary of the proposal

    Since: cosmos-sdk 0.47
    """
    proposer: builtins.str
    """proposer is the address of the proposal sumbitter

    Since: cosmos-sdk 0.47
    """
    expedited: builtins.bool
    """expedited defines if the proposal is expedited

    Since: cosmos-sdk 0.50
    Deprecated: Use ProposalType instead.
    """
    failed_reason: builtins.str
    """failed_reason defines the reason why the proposal failed

    Since: cosmos-sdk 0.50
    """
    proposal_type: global___ProposalType.ValueType
    """proposal_type defines the type of the proposal

    Since: x/gov v1.0.0
    """
    @property
    def messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """messages are the arbitrary messages to be executed if the proposal passes."""

    @property
    def final_tally_result(self) -> global___TallyResult:
        """final_tally_result is the final tally result of the proposal. When
        querying a proposal via gRPC, this field is not populated until the
        proposal's voting period has ended.
        """

    @property
    def submit_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """submit_time is the time of proposal submission."""

    @property
    def deposit_end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """deposit_end_time is the end time for deposition."""

    @property
    def total_deposit(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """total_deposit is the total deposit on the proposal."""

    @property
    def voting_start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """voting_start_time is the starting time to vote on a proposal."""

    @property
    def voting_end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """voting_end_time is the end time of voting on a proposal."""

    def __init__(
        self,
        *,
        id: builtins.int = ...,
        messages: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        status: global___ProposalStatus.ValueType = ...,
        final_tally_result: global___TallyResult | None = ...,
        submit_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        deposit_end_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        total_deposit: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        voting_start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        voting_end_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        metadata: builtins.str = ...,
        title: builtins.str = ...,
        summary: builtins.str = ...,
        proposer: builtins.str = ...,
        expedited: builtins.bool = ...,
        failed_reason: builtins.str = ...,
        proposal_type: global___ProposalType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["deposit_end_time", b"deposit_end_time", "final_tally_result", b"final_tally_result", "submit_time", b"submit_time", "voting_end_time", b"voting_end_time", "voting_start_time", b"voting_start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["deposit_end_time", b"deposit_end_time", "expedited", b"expedited", "failed_reason", b"failed_reason", "final_tally_result", b"final_tally_result", "id", b"id", "messages", b"messages", "metadata", b"metadata", "proposal_type", b"proposal_type", "proposer", b"proposer", "status", b"status", "submit_time", b"submit_time", "summary", b"summary", "title", b"title", "total_deposit", b"total_deposit", "voting_end_time", b"voting_end_time", "voting_start_time", b"voting_start_time"]) -> None: ...

global___Proposal = Proposal

@typing.final
class ProposalVoteOptions(google.protobuf.message.Message):
    """ProposalVoteOptions defines the stringified vote options for proposals.
    This allows to support multiple choice options for a given proposal.

    Since: x/gov v1.0.0
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPTION_ONE_FIELD_NUMBER: builtins.int
    OPTION_TWO_FIELD_NUMBER: builtins.int
    OPTION_THREE_FIELD_NUMBER: builtins.int
    OPTION_FOUR_FIELD_NUMBER: builtins.int
    OPTION_SPAM_FIELD_NUMBER: builtins.int
    option_one: builtins.str
    """option_one is the first option of the proposal"""
    option_two: builtins.str
    """option_two is the second option of the proposal"""
    option_three: builtins.str
    """option_three is the third option of the proposal"""
    option_four: builtins.str
    """option_four is the fourth option of the proposal"""
    option_spam: builtins.str
    """option_spam is always present for all proposals."""
    def __init__(
        self,
        *,
        option_one: builtins.str = ...,
        option_two: builtins.str = ...,
        option_three: builtins.str = ...,
        option_four: builtins.str = ...,
        option_spam: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["option_four", b"option_four", "option_one", b"option_one", "option_spam", b"option_spam", "option_three", b"option_three", "option_two", b"option_two"]) -> None: ...

global___ProposalVoteOptions = ProposalVoteOptions

@typing.final
class TallyResult(google.protobuf.message.Message):
    """TallyResult defines a standard tally for a governance proposal."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    YES_COUNT_FIELD_NUMBER: builtins.int
    ABSTAIN_COUNT_FIELD_NUMBER: builtins.int
    NO_COUNT_FIELD_NUMBER: builtins.int
    NO_WITH_VETO_COUNT_FIELD_NUMBER: builtins.int
    OPTION_ONE_COUNT_FIELD_NUMBER: builtins.int
    OPTION_TWO_COUNT_FIELD_NUMBER: builtins.int
    OPTION_THREE_COUNT_FIELD_NUMBER: builtins.int
    OPTION_FOUR_COUNT_FIELD_NUMBER: builtins.int
    SPAM_COUNT_FIELD_NUMBER: builtins.int
    yes_count: builtins.str
    """yes_count is the number of yes votes on a proposal.
    option 1
    """
    abstain_count: builtins.str
    """abstain_count is the number of abstain votes on a proposal.
    option 2
    """
    no_count: builtins.str
    """no_count is the number of no votes on a proposal.
    option 3
    """
    no_with_veto_count: builtins.str
    """no_with_veto_count is the number of no with veto votes on a proposal.
    option 4
    """
    option_one_count: builtins.str
    """option_one_count corresponds to the number of votes for option one (= yes_count for non multiple choice proposals)."""
    option_two_count: builtins.str
    """option_two_count corresponds to the number of votes for option two (= abstain_count for non multiple choice
    proposals).
    """
    option_three_count: builtins.str
    """option_three_count corresponds to the number of votes for option three (= no_count for non multiple choice
    proposals).
    """
    option_four_count: builtins.str
    """option_four_count corresponds to the number of votes for option four (= no_with_veto_count for non multiple choice
    proposals).
    """
    spam_count: builtins.str
    """spam_count is the number of spam votes on a proposal."""
    def __init__(
        self,
        *,
        yes_count: builtins.str = ...,
        abstain_count: builtins.str = ...,
        no_count: builtins.str = ...,
        no_with_veto_count: builtins.str = ...,
        option_one_count: builtins.str = ...,
        option_two_count: builtins.str = ...,
        option_three_count: builtins.str = ...,
        option_four_count: builtins.str = ...,
        spam_count: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["abstain_count", b"abstain_count", "no_count", b"no_count", "no_with_veto_count", b"no_with_veto_count", "option_four_count", b"option_four_count", "option_one_count", b"option_one_count", "option_three_count", b"option_three_count", "option_two_count", b"option_two_count", "spam_count", b"spam_count", "yes_count", b"yes_count"]) -> None: ...

global___TallyResult = TallyResult

@typing.final
class Vote(google.protobuf.message.Message):
    """Vote defines a vote on a governance proposal.
    A Vote consists of a proposal ID, the voter, and the vote option.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    VOTER_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    voter: builtins.str
    """voter is the voter address of the proposal."""
    metadata: builtins.str
    """metadata is any arbitrary metadata attached to the vote.
    the recommended format of the metadata is to be found here: https://docs.cosmos.network/v0.47/modules/gov#vote-5
    """
    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WeightedVoteOption]:
        """options is the weighted vote options."""

    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        voter: builtins.str = ...,
        options: collections.abc.Iterable[global___WeightedVoteOption] | None = ...,
        metadata: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "options", b"options", "proposal_id", b"proposal_id", "voter", b"voter"]) -> None: ...

global___Vote = Vote

@typing.final
class DepositParams(google.protobuf.message.Message):
    """DepositParams defines the params for deposits on governance proposals."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIN_DEPOSIT_FIELD_NUMBER: builtins.int
    MAX_DEPOSIT_PERIOD_FIELD_NUMBER: builtins.int
    @property
    def min_deposit(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """Minimum deposit for a proposal to enter voting period."""

    @property
    def max_deposit_period(self) -> google.protobuf.duration_pb2.Duration:
        """Maximum period for Atom holders to deposit on a proposal. Initial value: 2
        months.
        """

    def __init__(
        self,
        *,
        min_deposit: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        max_deposit_period: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["max_deposit_period", b"max_deposit_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["max_deposit_period", b"max_deposit_period", "min_deposit", b"min_deposit"]) -> None: ...

global___DepositParams = DepositParams

@typing.final
class VotingParams(google.protobuf.message.Message):
    """VotingParams defines the params for voting on governance proposals."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOTING_PERIOD_FIELD_NUMBER: builtins.int
    @property
    def voting_period(self) -> google.protobuf.duration_pb2.Duration:
        """Duration of the voting period."""

    def __init__(
        self,
        *,
        voting_period: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["voting_period", b"voting_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["voting_period", b"voting_period"]) -> None: ...

global___VotingParams = VotingParams

@typing.final
class TallyParams(google.protobuf.message.Message):
    """TallyParams defines the params for tallying votes on governance proposals."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUORUM_FIELD_NUMBER: builtins.int
    THRESHOLD_FIELD_NUMBER: builtins.int
    VETO_THRESHOLD_FIELD_NUMBER: builtins.int
    quorum: builtins.str
    """Minimum percentage of total stake needed to vote for a result to be
    considered valid.
    """
    threshold: builtins.str
    """Minimum proportion of Yes votes for proposal to pass. Default value: 0.5."""
    veto_threshold: builtins.str
    """Minimum value of Veto votes to Total votes ratio for proposal to be
    vetoed. Default value: 1/3.
    """
    def __init__(
        self,
        *,
        quorum: builtins.str = ...,
        threshold: builtins.str = ...,
        veto_threshold: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["quorum", b"quorum", "threshold", b"threshold", "veto_threshold", b"veto_threshold"]) -> None: ...

global___TallyParams = TallyParams

@typing.final
class Params(google.protobuf.message.Message):
    """Params defines the parameters for the x/gov module.

    Since: cosmos-sdk 0.47
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIN_DEPOSIT_FIELD_NUMBER: builtins.int
    MAX_DEPOSIT_PERIOD_FIELD_NUMBER: builtins.int
    VOTING_PERIOD_FIELD_NUMBER: builtins.int
    QUORUM_FIELD_NUMBER: builtins.int
    THRESHOLD_FIELD_NUMBER: builtins.int
    VETO_THRESHOLD_FIELD_NUMBER: builtins.int
    MIN_INITIAL_DEPOSIT_RATIO_FIELD_NUMBER: builtins.int
    PROPOSAL_CANCEL_RATIO_FIELD_NUMBER: builtins.int
    PROPOSAL_CANCEL_DEST_FIELD_NUMBER: builtins.int
    EXPEDITED_VOTING_PERIOD_FIELD_NUMBER: builtins.int
    EXPEDITED_THRESHOLD_FIELD_NUMBER: builtins.int
    EXPEDITED_MIN_DEPOSIT_FIELD_NUMBER: builtins.int
    BURN_VOTE_QUORUM_FIELD_NUMBER: builtins.int
    BURN_PROPOSAL_DEPOSIT_PREVOTE_FIELD_NUMBER: builtins.int
    BURN_VOTE_VETO_FIELD_NUMBER: builtins.int
    MIN_DEPOSIT_RATIO_FIELD_NUMBER: builtins.int
    PROPOSAL_CANCEL_MAX_PERIOD_FIELD_NUMBER: builtins.int
    OPTIMISTIC_AUTHORIZED_ADDRESSES_FIELD_NUMBER: builtins.int
    OPTIMISTIC_REJECTED_THRESHOLD_FIELD_NUMBER: builtins.int
    YES_QUORUM_FIELD_NUMBER: builtins.int
    quorum: builtins.str
    """ Minimum percentage of total stake needed to vote for a result to be
     considered valid.
    """
    threshold: builtins.str
    """ Minimum proportion of Yes votes for proposal to pass. Default value: 0.5."""
    veto_threshold: builtins.str
    """ Minimum value of Veto votes to Total votes ratio for proposal to be
     vetoed. Default value: 1/3.
    """
    min_initial_deposit_ratio: builtins.str
    """ The ratio representing the proportion of the deposit value that must be paid at proposal submission."""
    proposal_cancel_ratio: builtins.str
    """The cancel ratio which will not be returned back to the depositors when a proposal is cancelled.

    Since: cosmos-sdk 0.50
    """
    proposal_cancel_dest: builtins.str
    """The address which will receive (proposal_cancel_ratio * deposit) proposal deposits.
    If empty, the (proposal_cancel_ratio * deposit) proposal deposits will be burned.

    Since: cosmos-sdk 0.50
    """
    expedited_threshold: builtins.str
    """Minimum proportion of Yes votes for proposal to pass. Default value: 0.67.

    Since: cosmos-sdk 0.50
    """
    burn_vote_quorum: builtins.bool
    """burn deposits if a proposal does not meet quorum

    Since: cosmos-sdk 0.47
    """
    burn_proposal_deposit_prevote: builtins.bool
    """burn deposits if the proposal does not enter voting period

    Since: cosmos-sdk 0.47
    """
    burn_vote_veto: builtins.bool
    """burn deposits if quorum with vote type no_veto is met

    Since: cosmos-sdk 0.47
    """
    min_deposit_ratio: builtins.str
    """The ratio representing the proportion of the deposit value minimum that must be met when making a deposit.
    Default value: 0.01. Meaning that for a chain with a min_deposit of 100stake, a deposit of 1stake would be
    required.

    Since: cosmos-sdk 0.50
    """
    proposal_cancel_max_period: builtins.str
    """proposal_cancel_max_period defines how far in the voting period a proposer can cancel a proposal.
    If the proposal is cancelled before the max cancel period, the deposit will be returned/burn to the
    depositors, according to the proposal_cancel_ratio and proposal_cancel_dest parameters.
    After the max cancel period, the proposal cannot be cancelled anymore.

    Since: x/gov v1.0.0
    """
    optimistic_rejected_threshold: builtins.str
    """optimistic rejected threshold defines at which percentage of NO votes, the optimistic proposal should fail and be
    converted to a standard proposal. The threshold is expressed as a percentage of the total bonded tokens.

    Since: x/gov v1.0.0
    """
    yes_quorum: builtins.str
    """yes_quorum defines the minimum percentage of Yes votes in quorum for proposal to pass.
    Default value: 0 (disabled).

    Since: x/gov v1.0.0
    """
    @property
    def min_deposit(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """Minimum deposit for a proposal to enter voting period."""

    @property
    def max_deposit_period(self) -> google.protobuf.duration_pb2.Duration:
        """Maximum period for stake holders to deposit on a proposal. Initial value: 2
        months.
        """

    @property
    def voting_period(self) -> google.protobuf.duration_pb2.Duration:
        """Duration of the voting period."""

    @property
    def expedited_voting_period(self) -> google.protobuf.duration_pb2.Duration:
        """Duration of the voting period of an expedited proposal.

        Since: cosmos-sdk 0.50
        """

    @property
    def expedited_min_deposit(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """ Minimum expedited deposit for a proposal to enter voting period."""

    @property
    def optimistic_authorized_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """optimistic_authorized_addresses is an optional governance parameter that limits the authorized accounts than can
        submit optimistic proposals

        Since: x/gov v1.0.0
        """

    def __init__(
        self,
        *,
        min_deposit: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        max_deposit_period: google.protobuf.duration_pb2.Duration | None = ...,
        voting_period: google.protobuf.duration_pb2.Duration | None = ...,
        quorum: builtins.str = ...,
        threshold: builtins.str = ...,
        veto_threshold: builtins.str = ...,
        min_initial_deposit_ratio: builtins.str = ...,
        proposal_cancel_ratio: builtins.str = ...,
        proposal_cancel_dest: builtins.str = ...,
        expedited_voting_period: google.protobuf.duration_pb2.Duration | None = ...,
        expedited_threshold: builtins.str = ...,
        expedited_min_deposit: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        burn_vote_quorum: builtins.bool = ...,
        burn_proposal_deposit_prevote: builtins.bool = ...,
        burn_vote_veto: builtins.bool = ...,
        min_deposit_ratio: builtins.str = ...,
        proposal_cancel_max_period: builtins.str = ...,
        optimistic_authorized_addresses: collections.abc.Iterable[builtins.str] | None = ...,
        optimistic_rejected_threshold: builtins.str = ...,
        yes_quorum: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expedited_voting_period", b"expedited_voting_period", "max_deposit_period", b"max_deposit_period", "voting_period", b"voting_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["burn_proposal_deposit_prevote", b"burn_proposal_deposit_prevote", "burn_vote_quorum", b"burn_vote_quorum", "burn_vote_veto", b"burn_vote_veto", "expedited_min_deposit", b"expedited_min_deposit", "expedited_threshold", b"expedited_threshold", "expedited_voting_period", b"expedited_voting_period", "max_deposit_period", b"max_deposit_period", "min_deposit", b"min_deposit", "min_deposit_ratio", b"min_deposit_ratio", "min_initial_deposit_ratio", b"min_initial_deposit_ratio", "optimistic_authorized_addresses", b"optimistic_authorized_addresses", "optimistic_rejected_threshold", b"optimistic_rejected_threshold", "proposal_cancel_dest", b"proposal_cancel_dest", "proposal_cancel_max_period", b"proposal_cancel_max_period", "proposal_cancel_ratio", b"proposal_cancel_ratio", "quorum", b"quorum", "threshold", b"threshold", "veto_threshold", b"veto_threshold", "voting_period", b"voting_period", "yes_quorum", b"yes_quorum"]) -> None: ...

global___Params = Params

@typing.final
class MessageBasedParams(google.protobuf.message.Message):
    """MessageBasedParams defines the parameters of specific messages in a proposal.
    It is used to define the parameters of a proposal that is based on a specific message.
    Once a message has message based params, it only supports a standard proposal type.

    Since: x/gov v1.0.0
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOTING_PERIOD_FIELD_NUMBER: builtins.int
    QUORUM_FIELD_NUMBER: builtins.int
    YES_QUORUM_FIELD_NUMBER: builtins.int
    THRESHOLD_FIELD_NUMBER: builtins.int
    VETO_THRESHOLD_FIELD_NUMBER: builtins.int
    quorum: builtins.str
    """Minimum percentage of total stake needed to vote for a result to be considered valid."""
    yes_quorum: builtins.str
    """yes_quorum defines the minimum percentage of Yes votes in quorum for proposal to pass.
    If zero then the yes_quorum is disabled.
    """
    threshold: builtins.str
    """Minimum proportion of Yes votes for proposal to pass."""
    veto_threshold: builtins.str
    """Minimum value of Veto votes to Total votes ratio for proposal to be vetoed."""
    @property
    def voting_period(self) -> google.protobuf.duration_pb2.Duration:
        """Duration of the voting period."""

    def __init__(
        self,
        *,
        voting_period: google.protobuf.duration_pb2.Duration | None = ...,
        quorum: builtins.str = ...,
        yes_quorum: builtins.str = ...,
        threshold: builtins.str = ...,
        veto_threshold: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["voting_period", b"voting_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["quorum", b"quorum", "threshold", b"threshold", "veto_threshold", b"veto_threshold", "voting_period", b"voting_period", "yes_quorum", b"yes_quorum"]) -> None: ...

global___MessageBasedParams = MessageBasedParams
