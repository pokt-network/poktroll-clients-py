from src.block_client import BlockQueryClient
from src.depinject import Supply
from src.events_query_client import EventsQueryClient


def test_depinject_supply():
    client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    cfg_ref = Supply(client.go_ref)


def test_depinject_supply_many():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
