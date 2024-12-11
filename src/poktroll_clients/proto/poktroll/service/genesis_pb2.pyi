"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import poktroll.service.params_pb2
import poktroll.service.relay_mining_difficulty_pb2
import poktroll.shared.service_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the service module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    SERVICE_LIST_FIELD_NUMBER: builtins.int
    RELAYMININGDIFFICULTYLIST_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> poktroll.service.params_pb2.Params:
        """params defines all the parameters of the module."""

    @property
    def service_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[poktroll.shared.service_pb2.Service]: ...
    @property
    def relayMiningDifficultyList(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[poktroll.service.relay_mining_difficulty_pb2.RelayMiningDifficulty]: ...
    def __init__(
        self,
        *,
        params: poktroll.service.params_pb2.Params | None = ...,
        service_list: collections.abc.Iterable[poktroll.shared.service_pb2.Service] | None = ...,
        relayMiningDifficultyList: collections.abc.Iterable[poktroll.service.relay_mining_difficulty_pb2.RelayMiningDifficulty] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["params", b"params", "relayMiningDifficultyList", b"relayMiningDifficultyList", "service_list", b"service_list"]) -> None: ...

global___GenesisState = GenesisState
