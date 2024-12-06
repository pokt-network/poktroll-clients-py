import pytest
from gen.cosmos.base.v1beta1.coin_pb2 import Coin
from gen.poktroll.shared.service_pb2 import ApplicationServiceConfig
from gen.poktroll.application.tx_pb2 import MsgStakeApplication, MsgUnstakeApplication
from src.block_client import BlockClient, BlockQueryClient
from src.depinject import SupplyMany
from src.events_query_client import EventsQueryClient
from src.go_memory import go_ref
from src.tx_client import TxContext, TxClient


def test_tx_context():
    tx_ctx = TxContext("tcp://127.0.0.1:26657")


def test_tx_client():
    cfg_ref = get_tx_client_deps()
    tx_client = TxClient(cfg_ref, "faucet")


@pytest.mark.asyncio
async def test_sign_and_broadcast():
    cfg_ref = get_tx_client_deps()
    tx_client = TxClient(cfg_ref, "app3")

    stake_app3_msg = MsgStakeApplication(
        address="pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex",
        stake=Coin(denom="upokt", amount="100000000"),
        services=[ApplicationServiceConfig(service_id="anvil")]
    )

    try:
        await tx_client.SignAndBroadcast(stake_app3_msg)

        unstake_app3_msg = MsgUnstakeApplication(
            address="pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex"
        )
        await tx_client.SignAndBroadcast(unstake_app3_msg)
    except Exception as e:
        pytest.fail(f"SignAndBroadcast failed with error: {str(e)}")


@pytest.mark.asyncio
async def test_sign_and_broadcast_error():
    cfg_ref = get_tx_client_deps()
    tx_client = TxClient(cfg_ref, "app1")

    # Attempt to stake an already-staked address (app1)
    stake_app1_msg = MsgStakeApplication(
        address="pokt1mrqt5f7qh8uxs27cjm9t7v9e74a9vvdnq5jva4",
        stake=Coin(denom="upokt", amount="1"),
        services=[ApplicationServiceConfig(service_id="anvil")]
    )

    with pytest.raises(Exception,
                      match=r"(.*failed to execute message.*stake amount.*must be higher than previous stake amount.*|.*EOF: error encountered while querying for tx.*)"):
        await tx_client.SignAndBroadcast(stake_app1_msg)


def get_tx_client_deps() -> go_ref:
    events_query_client = EventsQueryClient("ws://127.0.0.1:26657/websocket")
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")

    cfg_ref = SupplyMany(events_query_client, block_query_client)
    block_client = BlockClient(cfg_ref)

    tx_ctx = TxContext("tcp://127.0.0.1:26657")

    return SupplyMany(events_query_client, block_client, tx_ctx)