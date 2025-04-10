from pocket_clients.proto.pocket.gateway.types_pb2 import Gateway
from pocket_clients.query_client import QueryClient

gateway1_addr = "pokt15vzxjqklzjtlz7lahe8z2dfe9nm5vxwwmscne4"


# def test_query_gateway():
#     query_client = QueryClient("http://127.0.0.1:26657")
#
#     expected_gateway1 = Gateway(address=gateway1_addr)
#     gateway1 = query_client.get_gateway(gateway1_addr)
#     assert gateway1 == expected_gateway1
#
#
# async def test_query_all_gateways():
#     expected_gateway_addrs = [gateway1_addr]
#     query_client = QueryClient("http://127.0.0.1:26657")
#     gateways = query_client.get_all_gateways()
#     assert len(gateways) == 2
#     assert set([gateway.address for gateway in gateways]) == set(expected_gateway_addrs)
