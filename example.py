from pprint import pprint
import asyncio
from poktroll_clients.proto.poktroll.application.tx_pb2 import *
from poktroll_clients.proto.poktroll.shared.service_pb2 import *
from poktroll_clients.proto.cosmos.base.v1beta1.coin_pb2 import *
from poktroll_clients import (
    TxClient,
    QueryClient,
)

"""
Signing key name should match the name of a key in the local poktrolld keyring
which is authorized to sign for any transactions the tx client will broadcast.
See `poktrolld keys -h` for more information.
"""
signing_key_name = "key-name"

"""
Query node RPC URL is the HTTP URL for the poktroll RPC endpoint to which query
clients will send requests.
"""
# query_node_rpc_url = "http://127.0.0.1:26657"
query_node_rpc_url = "https://shannon-testnet-grove-rpc.beta.poktroll.com"

"""
Tx node RPC URL is the gRPC gateway URL for the poktroll RPC endpoint to which the
tx client will connect and broadcast signed transactions. It MUST use the tcp:// scheme.
"""
# tx_node_rpc_url = "tcp://127.0.0.1:26657"
tx_node_rpc_url = "https://shannon-testnet-grove-grpc.beta.poktroll.com"

tx_client = TxClient(
    signing_key_name,
    query_node_rpc_url=query_node_rpc_url,
    tx_node_rpc_url=tx_node_rpc_url,
)

query_client = QueryClient(query_node_rpc_url)

app3_addr = "pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex"
gateway1_addr = "pokt15vzxjqklzjtlz7lahe8z2dfe9nm5vxwwmscne4"
gateway2_addr = "pokt15w3fhfyc0lttv7r585e2ncpf6t2kl9uh8rsnyz"


async def main():
    # Application 3 tx client (app3 SHOULD NOT be staked)
    app_tx_client = TxClient(
        "app3", query_node_rpc_url=query_node_rpc_url, tx_node_rpc_url=tx_node_rpc_url
    )

    # Stake and delegate application 3 to gateways 1 (in one tx)
    await app_tx_client.sign_and_broadcast(
        MsgStakeApplication(
            address="pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex",
            stake=Coin(denom="upokt", amount="100000000"),
            services=[ApplicationServiceConfig(service_id="anvil")],
        ),
        *[
            MsgDelegateToGateway(
                app_address=app3_addr,
                gateway_address=gateway_addr,
            )
            for gateway_addr in [gateway1_addr, gateway2_addr]
        ],
    )

    # Query all applications
    applications = query_client.get_all_applications()
    pprint(applications)

    # Unstake application 3
    await app_tx_client.sign_and_broadcast(
        MsgUnstakeApplication(address=app3_addr),
    )


if __name__ == "__main__":
    asyncio.run(main())
