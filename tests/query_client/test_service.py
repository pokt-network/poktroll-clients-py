from base64 import b64decode

from pocket_clients import BlockQueryClient
from pocket_clients.proto.pocket.service.relay_mining_difficulty_pb2 import RelayMiningDifficulty
from pocket_clients.proto.pocket.shared.service_pb2 import Service
from pocket_clients.query_client import QueryClient


def test_query_get_service():
    query_client = QueryClient("http://127.0.0.1:26657")

    expected_service = Service(
        id="anvil",
        name="anvil",
        owner_address="pokt1cwnu460557x0z78jv3hhc7356hhkrgc86c87q5",
        compute_units_per_relay=1,
    )
    service1 = query_client.get_service("anvil")
    assert service1 == expected_service


def test_query_get_service_relay_difficulty():
    # TODO_CONSIDERATION: compose a block query client into the query client.
    block_query_client = BlockQueryClient("http://127.0.0.1:26657")
    current_height = block_query_client.block().header.height

    query_client = QueryClient("http://127.0.0.1:26657")

    expected_service_relay_difficulty = RelayMiningDifficulty(
        service_id="anvil",
        block_height=current_height,
        num_relays_ema=100000,
        target_hash=b64decode(b"//////////////////////////////////////////8="),
    )

    service_relay_difficulty = query_client.get_service_relay_difficulty("anvil")
    assert service_relay_difficulty == expected_service_relay_difficulty
