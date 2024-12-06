from src.block_client import BlockQueryClient, BlockClient
from src.depinject import SupplyMany
from src.events_query_client import EventsQueryClient


def test_block_query_client():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")


def test_block_client():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    cfg_ref = SupplyMany(events_query_client, block_query_client)
    block_client = BlockClient(cfg_ref)
