import sys
from os import path

# TODO_IN_THIS_COMMIT: figure out why this is being problematic....
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), "../src")))

import pytest
# from src.poktroll_clients import EventsQueryClient
from poktroll_clients import EventsQueryClient


def test_events_query_client():
    client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    assert client.selfRef != -1
    assert client.selfRef != 0
    assert client.EventsBytes("tm.event='Tx'") != -1
    assert client.EventsBytes("tm.event='Tx'") != 0
