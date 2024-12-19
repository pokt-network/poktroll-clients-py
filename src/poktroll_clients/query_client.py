from poktroll_clients import (
    go_ref,
    ffi,
    libpoktroll_clients,
    GoManagedMem, BlockQueryClient, Supply, check_err, check_ref,
)
from poktroll_clients.proto.poktroll.session.params_pb2 import Params as SessionParams
from poktroll_clients.proto.poktroll.shared.params_pb2 import Params as SharedParams
from poktroll_clients.proto.poktroll.proof.params_pb2 import Params as ProofParams
from poktroll_clients.proto.poktroll.application.params_pb2 import Params as ApplicationParams
from poktroll_clients.protobuf import get_proto_from_go_ref


class QueryClient(GoManagedMem):
    """
    A client which can query for any poktroll module state.
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, query_node_rpc_url: str, deps_ref: go_ref = -1):
        if deps_ref == -1:
            deps_ref = _new_query_client_depinject_config(query_node_rpc_url)

        self_ref = libpoktroll_clients.NewQueryClient(deps_ref,
                                                      query_node_rpc_url.encode('utf-8'),
                                                      self.err_ptr)
        super().__init__(self_ref)

    def get_shared_params(self) -> SharedParams:
        params_ref = libpoktroll_clients.QueryClient_GetSharedParams(self.go_ref, self.err_ptr)
        check_err(self.err_ptr)
        check_ref(params_ref)

        return get_proto_from_go_ref(params_ref)

    def get_application_params(self) -> ApplicationParams:
        params_ref = libpoktroll_clients.QueryClient_GetApplicationParams(self.go_ref, self.err_ptr)
        check_err(self.err_ptr)
        check_ref(params_ref)

        return get_proto_from_go_ref(params_ref)

    # TODO_BLOCKED(@bryanchriswhite, poktroll#534): add commented methods once
    # Go method dependencies are available.

    # def get_supplier_params(self) -> SupplierParams:
    #     response_ref = libpoktroll_clients.QueryClient_GetSupplierParams(self.go_ref, self.err_ptr)

    # def get_gateway_params(self) -> GatewayParams:
    #     response_ref = libpoktroll_clients.QueryClient_GetGatewayParams(self.go_ref, self.err_ptr)

    def get_session_params(self) -> SessionParams:
        params_ref = libpoktroll_clients.QueryClient_GetSessionParams(self.go_ref, self.err_ptr)

        check_err(self.err_ptr)
        check_ref(params_ref)

        return get_proto_from_go_ref(params_ref)

    # def get_service_params(self) -> ServiceParams:
    #     response_ref = libpoktroll_clients.QueryClient_GetServiceParams(self.go_ref, self.err_ptr)

    def get_proof_params(self) -> ProofParams:
        params_ref = libpoktroll_clients.QueryClient_GetProofParams(self.go_ref, self.err_ptr)

        check_err(self.err_ptr)
        check_ref(params_ref)

        return get_proto_from_go_ref(params_ref)

    # def get_tokenomics_params(self) -> TokenomicsParams:
    #     response_ref = libpoktroll_clients.QueryClient_GetTokenomicsParams(self.go_ref, self.err_ptr)


def _new_query_client_depinject_config(
        query_node_rpc_url: str,
) -> go_ref:
    """
    Construct the required dependencies for the query client:
    - BlockQueryClient

    Args:
        query_node_rpc_url: The URL of the query node RPC server.
    Returns:
        A go_ref reference to the depinject config which contains the Go dependencies.
    Raises:
        ValueError: If the query_node_rpc_url is not specified.
    """

    # TODO_IN_THIS_COMMIT: add more detail to the error messages,
    # explaining the expected format, with an example.
    if not query_node_rpc_url:
        raise ValueError("query_node_rpc_url must be specified")

    block_query_client = BlockQueryClient(query_node_rpc_url)
    return Supply(block_query_client.go_ref)
