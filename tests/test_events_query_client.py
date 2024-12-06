from src.events_query_client import EventsQueryClient


def test_events_query_client():
    client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    assert client.EventsBytes("tm.event='Tx'") != -1
    assert client.EventsBytes("tm.event='Tx'") != 0
