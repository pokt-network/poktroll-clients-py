from asyncio import sleep

import cffi
import pytest

from poktroll_clients import TxClient
from poktroll_clients.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from poktroll_clients.proto.poktroll.application.tx_pb2 import MsgStakeApplication, MsgUnstakeApplication
from poktroll_clients.proto.poktroll.application.types_pb2 import Application
from poktroll_clients.proto.poktroll.shared.service_pb2 import SupplierServiceConfig, SupplierEndpoint, JSON_RPC, \
    ApplicationServiceConfig
from poktroll_clients.query_client import QueryClient

app1_addr = "pokt1mrqt5f7qh8uxs27cjm9t7v9e74a9vvdnq5jva4"
app3_addr = "pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex"
gateway1_addr = "pokt15vzxjqklzjtlz7lahe8z2dfe9nm5vxwwmscne4"


def test_query_application():
    query_client = QueryClient("http://127.0.0.1:26657")

    expected_app1 = Application(
        address=app1_addr,
        stake=Coin(amount="100000068", denom="upokt"),
        delegatee_gateway_addresses=[gateway1_addr],
        service_configs=[ApplicationServiceConfig(service_id="anvil")],
        unstake_session_end_height=0,
    )
    app1 = query_client.get_application(app1_addr)
    assert app1 == expected_app1


@pytest.mark.asyncio
async def test_query_all_applications():
    expected_app_addrs = [app1_addr]
    query_client = QueryClient("http://127.0.0.1:26657")
    apps = query_client.get_all_applications()
    assert len(apps) == 1
    assert set([app.address for app in apps]) == set(expected_app_addrs)
