from typing_extensions import assert_type

from poktroll_clients import (
    BlockQueryClient,
    BlockClient,
    EventsQueryClient,
    SupplyMany,
)
from poktroll_clients.proto.tendermint.types.block_pb2 import Block


def test_block_query_client():
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    current_block = block_query_client.block()

    assert_type(current_block, Block)
    assert current_block.header.height != 0



def test_block_client():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    deps_ref = SupplyMany(events_query_client, block_query_client)
    block_client = BlockClient(deps_ref)
