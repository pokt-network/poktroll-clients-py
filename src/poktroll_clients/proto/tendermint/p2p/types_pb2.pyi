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
class NetAddress(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    IP_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    id: builtins.str
    ip: builtins.str
    port: builtins.int
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        ip: builtins.str = ...,
        port: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "ip", b"ip", "port", b"port"]) -> None: ...

global___NetAddress = NetAddress

@typing.final
class ProtocolVersion(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    P2P_FIELD_NUMBER: builtins.int
    BLOCK_FIELD_NUMBER: builtins.int
    APP_FIELD_NUMBER: builtins.int
    p2p: builtins.int
    block: builtins.int
    app: builtins.int
    def __init__(
        self,
        *,
        p2p: builtins.int = ...,
        block: builtins.int = ...,
        app: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["app", b"app", "block", b"block", "p2p", b"p2p"]) -> None: ...

global___ProtocolVersion = ProtocolVersion

@typing.final
class DefaultNodeInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROTOCOL_VERSION_FIELD_NUMBER: builtins.int
    DEFAULT_NODE_ID_FIELD_NUMBER: builtins.int
    LISTEN_ADDR_FIELD_NUMBER: builtins.int
    NETWORK_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    CHANNELS_FIELD_NUMBER: builtins.int
    MONIKER_FIELD_NUMBER: builtins.int
    OTHER_FIELD_NUMBER: builtins.int
    default_node_id: builtins.str
    listen_addr: builtins.str
    network: builtins.str
    version: builtins.str
    channels: builtins.bytes
    moniker: builtins.str
    @property
    def protocol_version(self) -> global___ProtocolVersion: ...
    @property
    def other(self) -> global___DefaultNodeInfoOther: ...
    def __init__(
        self,
        *,
        protocol_version: global___ProtocolVersion | None = ...,
        default_node_id: builtins.str = ...,
        listen_addr: builtins.str = ...,
        network: builtins.str = ...,
        version: builtins.str = ...,
        channels: builtins.bytes = ...,
        moniker: builtins.str = ...,
        other: global___DefaultNodeInfoOther | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["other", b"other", "protocol_version", b"protocol_version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["channels", b"channels", "default_node_id", b"default_node_id", "listen_addr", b"listen_addr", "moniker", b"moniker", "network", b"network", "other", b"other", "protocol_version", b"protocol_version", "version", b"version"]) -> None: ...

global___DefaultNodeInfo = DefaultNodeInfo

@typing.final
class DefaultNodeInfoOther(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_INDEX_FIELD_NUMBER: builtins.int
    RPC_ADDRESS_FIELD_NUMBER: builtins.int
    tx_index: builtins.str
    rpc_address: builtins.str
    def __init__(
        self,
        *,
        tx_index: builtins.str = ...,
        rpc_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["rpc_address", b"rpc_address", "tx_index", b"tx_index"]) -> None: ...

global___DefaultNodeInfoOther = DefaultNodeInfoOther