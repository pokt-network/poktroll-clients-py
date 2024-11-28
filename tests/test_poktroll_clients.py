import sys
from os import path

# TODO_IN_THIS_COMMIT: figure out why this is being problematic....
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), "../src")))

import pytest
from poktroll_clients import *


def test_events_query_client():
    client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    # TODO_IN_THIS_COMMIT: refactor constructor to error if selfRef is < 1.
    assert client.EventsBytes("tm.event='Tx'") != -1
    assert client.EventsBytes("tm.event='Tx'") != 0


def test_depinject_supply():
    client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    cfg_ref = Supply(client.go_ref)


def test_block_query_client():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")


def test_depinject_supply_many():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")


def test_tx_context():
    tx_ctx = TxContext("tcp://127.0.0.1:26657")


def test_block_client():
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    cfg_ref = SupplyMany(events_query_client, block_query_client)
    block_client = BlockClient(cfg_ref)


def test_tx_client():
    cfg_ref = get_tx_client_deps()
    tx_client = TxClient(cfg_ref, "faucet")


def test_sign_and_broadcast():
    cfg_ref = get_tx_client_deps()
    tx_client = TxClient(cfg_ref, "faucet")

    # NB: MsgSend from faucet to app1.
    send_msg_any_json = """
    {
      "@type": "type.googleapis.com/cosmos.bank.v1beta1.MsgSend",
      "from_address": "pokt1awtlw5sjmw2f5lgj8ekdkaqezphgz88rdk93sk",
      "to_address": "pokt1mrqt5f7qh8uxs27cjm9t7v9e74a9vvdnq5jva4",
      "amount": [
        {
          "denom": "upokt",
          "amount": "100000000"
        }
      ]
    }
    """

    err_ch_ref = tx_client.SignAndBroadcast(send_msg_any_json)


def get_tx_client_deps() -> GoRef:
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")

    cfg_ref = SupplyMany(events_query_client, block_query_client)
    block_client = BlockClient(cfg_ref)

    tx_ctx = TxContext("tcp://127.0.0.1:26657")

    return SupplyMany(events_query_client, block_client, tx_ctx)
