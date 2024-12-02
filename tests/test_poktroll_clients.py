import sys
from os import path
import pytest
from src.poktroll_clients import *
from gen.cosmos.base.v1beta1.coin_pb2 import Coin
from gen.poktroll.shared.service_pb2 import ApplicationServiceConfig
from gen.poktroll.shared.service_pb2 import Service
from gen.poktroll.application.tx_pb2 import MsgStakeApplication, MsgUnstakeApplication


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


def test_sign_and_broadcast_any():
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

    err_ch_ref = tx_client.SignAndBroadcastAny(send_msg_any_json)


def test_sign_and_broadcast():
    # NB: Unstaking app1.
    # unstakeApp1Msg = MsgUnstakeApplication(address="pokt1mrqt5f7qh8uxs27cjm9t7v9e74a9vvdnq5jva4")

    stakeApp3Msg = MsgStakeApplication(address="pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex",
                                       stake=(Coin(denom="upokt", amount="100000000")),
                                       services=[(ApplicationServiceConfig(service_id="svc1"))])

    cfg_ref = get_tx_client_deps()
    tx_client = TxClient(cfg_ref, "app3")

    # fut = tx_client.SignAndBroadcast(unstakeApp1Msg)
    # fut.result()
    # # loop = asyncio.get_running_loop()
    # # result = loop.run_until_complete(fut)

    fut = tx_client.SignAndBroadcast(stakeApp3Msg)
    fut.result()


def get_tx_client_deps() -> go_ref:
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")

    cfg_ref = SupplyMany(events_query_client, block_query_client)
    block_client = BlockClient(cfg_ref)

    tx_ctx = TxContext("tcp://127.0.0.1:26657")

    return SupplyMany(events_query_client, block_client, tx_ctx)
