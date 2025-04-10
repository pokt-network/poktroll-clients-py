from pocket_clients.proto.pocket.session.params_pb2 import Params as SessionParams
from pocket_clients.query_client import QueryClient

app1_addr = "pokt1mrqt5f7qh8uxs27cjm9t7v9e74a9vvdnq5jva4"


def test_query_session_params():
    query_client = QueryClient("http://127.0.0.1:26657")

    session_params = query_client.get_session_params()

    expected_session_params = SessionParams(
        num_suppliers_per_session=15,
    )

    assert session_params == expected_session_params


def test_query_get_session():
    query_client = QueryClient("http://127.0.0.1:26657")

    session = query_client.get_session(app1_addr, "anvil", 1)
    assert session.header.session_id == "de098a69e302007744dfd7a31df5dc5782b0c3a81f0b092e6c34865587e3089f"
    assert session.header.session_start_block_height == 1
    assert session.header.session_end_block_height == 10
    assert session.header.application_address == app1_addr
    assert session.header.service_id == "anvil"
