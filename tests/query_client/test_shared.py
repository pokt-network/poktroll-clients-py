from poktroll_clients import BlockQueryClient
from poktroll_clients.proto.poktroll.shared.params_pb2 import Params as SharedParams
from poktroll_clients.query_client import QueryClient


def test_query_shared_session_windows():
    query_node_rpc_url = "http://127.0.0.1:26657"

    block_query_client = BlockQueryClient(query_node_rpc_url)
    current_block = block_query_client.block()
    current_height = current_block.header.height

    query_client = QueryClient(query_node_rpc_url)
    shared_params = query_client.get_shared_params()

    # Ensure that the test height is old enough that we are able to calculate the
    # corresponding session claim and proof window heights.
    test_height = current_height - (shared_params.num_blocks_per_session * 5)

    # TODO_TECHDEBT(poktroll): Add SharedQueryClient#GetSessionEndHeight
    # session_end_height = query_client.get_session_end_height(current_height)
    # assert (current_height + shared_params.num_blocks_per_session
    #         <= session_end_height >
    #         current_height - shared_params.num_blocks_per_session)

    # expected_grace_period_end_height = session_end_height + shared_params.grace_period_end_offset_blocks
    session_grace_period_end_height = query_client.get_session_grace_period_end_height(test_height)
    max_grace_period_end_height = test_height + shared_params.grace_period_end_offset_blocks + int(
        shared_params.num_blocks_per_session)
    min_grace_period_end_height = test_height + shared_params.grace_period_end_offset_blocks - int(
        shared_params.num_blocks_per_session)
    assert min_grace_period_end_height < session_grace_period_end_height < max_grace_period_end_height

    # expected_claim_window_open_height = session_end_height +
    # shared_params.grace_period_end_offset_blocks +
    # shared_params.claim_window_open_offset_blocks
    claim_window_open_height = query_client.get_claim_window_open_height(test_height)
    max_claim_window_open_height = max_grace_period_end_height + shared_params.claim_window_open_offset_blocks
    min_claim_window_open_height = min_grace_period_end_height + shared_params.claim_window_open_offset_blocks
    assert min_claim_window_open_height < claim_window_open_height < max_claim_window_open_height

    claim_window_close_height = query_client.get_earliest_supplier_claim_commit_height(
        test_height, "pokt1mrqt5f7qh8uxs27cjm9t7v9e74a9vvdnq5jva4")
    max_claim_window_close_height = max_claim_window_open_height + shared_params.claim_window_close_offset_blocks
    min_claim_window_close_height = min_claim_window_open_height + shared_params.claim_window_close_offset_blocks
    assert min_claim_window_close_height < claim_window_close_height < max_claim_window_close_height

    proof_window_open_height = query_client.get_proof_window_open_height(test_height)
    max_proof_window_open_height = max_claim_window_close_height + shared_params.proof_window_open_offset_blocks
    min_proof_window_open_height = min_claim_window_close_height + shared_params.proof_window_open_offset_blocks
    print(f"max_proof_window_open_height: {max_proof_window_open_height}")
    print(f"min_proof_window_open_height: {min_proof_window_open_height}")
    print(f"proof_window_open_height: {proof_window_open_height}")
    assert min_proof_window_open_height < proof_window_open_height < max_proof_window_open_height

    proof_window_close_height = query_client.get_earliest_supplier_proof_commit_height(
        test_height, "pokt1mrqt5f7qh8uxs27cjm9t7v9e74a9vvdnq5jva4")
    max_proof_window_close_height = max_proof_window_open_height + shared_params.proof_window_close_offset_blocks
    min_proof_window_close_height = min_proof_window_open_height + shared_params.proof_window_close_offset_blocks
    assert min_proof_window_close_height < proof_window_close_height < max_proof_window_close_height

    compute_units_to_tokens_multiplier = query_client.get_compute_units_to_tokens_multiplier()
    assert compute_units_to_tokens_multiplier == shared_params.compute_units_to_tokens_multiplier


def test_query_shared_params():
    query_client = QueryClient("http://127.0.0.1:26657")

    # TODO_CONSIDERATION: async API for query methods.
    # shared_params = await query_client.get_shared_params()
    shared_params = query_client.get_shared_params()

    expected_shared_params = SharedParams(
        num_blocks_per_session=10,
        grace_period_end_offset_blocks=1,
        claim_window_open_offset_blocks=1,
        claim_window_close_offset_blocks=4,
        proof_window_close_offset_blocks=4,
        supplier_unbonding_period_sessions=1,
        application_unbonding_period_sessions=1,
        compute_units_to_tokens_multiplier=42,
    )

    assert shared_params == expected_shared_params
