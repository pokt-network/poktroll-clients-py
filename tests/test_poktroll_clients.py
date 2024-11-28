import sys
from os import path

# TODO_IN_THIS_COMMIT: figure out why this is being problematic....
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), "../src")))

import pytest
# from src.poktroll_clients import EventsQueryClient
from poktroll_clients import *


def test_events_query_client():
    client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    # TODO_IN_THIS_COMMIT: refactor constructor to error if selfRef is < 1.
    assert client.self_ref != -1
    assert client.self_ref != 0
    assert client.EventsBytes("tm.event='Tx'") != -1
    assert client.EventsBytes("tm.event='Tx'") != 0


def test_block_query_client():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    assert events_query_client.self_ref != -1
    assert events_query_client.self_ref != 0

    # TODO_IN_THIS_COMMIT: refactor constructor to error if selfRef is < 1.
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    assert events_query_client.self_ref != -1
    assert events_query_client.self_ref != 0
