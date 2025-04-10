from pocket_clients.ffi import ffi, libpocket_clients
from pocket_clients.go_memory import GoManagedMem, go_ref


class EventsQueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, query_node_rpc_websocket_url: str):
        self_ref = libpocket_clients.NewEventsQueryClient(query_node_rpc_websocket_url.encode('utf-8'))
        super().__init__(self_ref)

    def EventsBytes(self, query: str) -> go_ref:
        return libpocket_clients.EventsQueryClientEventsBytes(self.go_ref, query.encode('utf-8'))
