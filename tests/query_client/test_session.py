from poktroll_clients.proto.poktroll.session.params_pb2 import Params as SessionParams
from poktroll_clients.query_client import QueryClient


# @pytest.mark.asyncio


def test_query_session_params():
    query_client = QueryClient("http://127.0.0.1:26657")

    session_params = query_client.get_session_params()

    expected_session_params = SessionParams(
        num_suppliers_per_session=15,
    )

    assert session_params == expected_session_params
