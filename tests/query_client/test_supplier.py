from pocket_clients.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pocket_clients.proto.pocket.shared.service_pb2 import ApplicationServiceConfig, SupplierServiceConfig, \
    SupplierEndpoint, JSON_RPC, ServiceRevenueShare, REST
from pocket_clients.proto.pocket.shared.supplier_pb2 import Supplier
from pocket_clients.query_client import QueryClient

supplier1_addr = "pokt19a3t4yunp0dlpfjrp7qwnzwlrzd5fzs2gjaaaj"


def test_query_supplier():
    query_client = QueryClient("http://127.0.0.1:26657")

    expected_supplier1 = Supplier(
        operator_address=supplier1_addr,
        owner_address=supplier1_addr,
        stake=Coin(amount="1000068", denom="upokt"),
        services=[
            SupplierServiceConfig(
                service_id="anvil",
                endpoints=[
                    SupplierEndpoint(
                        url="http://relayminer1:8545",
                        rpc_type=JSON_RPC,
                        configs=[]
                    )
                ],
                rev_share=[
                    ServiceRevenueShare(
                        address="pokt19a3t4yunp0dlpfjrp7qwnzwlrzd5fzs2gjaaaj",
                        rev_share_percentage=100
                    )
                ]
            ),
            SupplierServiceConfig(
                service_id="rest",
                endpoints=[
                    SupplierEndpoint(
                        url="http://relayminer1:8545",
                        rpc_type=REST,
                        configs=[]
                    )
                ],
                rev_share=[
                    ServiceRevenueShare(
                        address="pokt19a3t4yunp0dlpfjrp7qwnzwlrzd5fzs2gjaaaj",
                        rev_share_percentage=100
                    )
                ]
            ),
            SupplierServiceConfig(
                service_id="ollama",
                endpoints=[
                    SupplierEndpoint(
                        url="http://relayminer1:8545",
                        rpc_type=REST,
                        configs=[]
                    )
                ],
                rev_share=[
                    ServiceRevenueShare(
                        address="pokt19a3t4yunp0dlpfjrp7qwnzwlrzd5fzs2gjaaaj",
                        rev_share_percentage=100
                    )
                ]
            )
        ],
        services_activation_heights_map={},
        unstake_session_end_height=0,
    )

    supplier1 = query_client.get_supplier(supplier1_addr)
    assert supplier1 == expected_supplier1

# async def test_query_all_suppliers():
#     expected_supplier_addrs = [supplier1_addr]
#     query_client = QueryClient("http://127.0.0.1:26657")
#     suppliers = query_client.get_all_suppliers()
#     assert len(suppliers) == 2
#     assert set([supplier.address for supplier in suppliers]) == set(expected_supplier_addrs)
