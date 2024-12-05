import asyncio
import importlib
from concurrent.futures import Future
from os import path
from typing import Union, Optional, Dict, Tuple, Callable

from atomics import INTEGRAL, atomic, INT
from google.protobuf.message import Message

from cffi import FFI

go_ref = int

# Initialize CFFI
ffi = FFI()

# TODO_IN_THIS_COMMIT: comment
callback_type = Callable[[ffi.CData, ffi.CData], None]

# Load and read the header file contents
thisDirPath = path.dirname(path.abspath(__file__))

# Add complete struct definitions for CFFI
ffi.cdef("""
    typedef struct {
        unsigned char __size[40];
        long int __align;
    } pthread_mutex_t;

    typedef struct {
        unsigned char __size[48];
        long long int __align;
    } pthread_cond_t;
    
    typedef struct AsyncContext {
        pthread_mutex_t mutex;
        pthread_cond_t cond;
        bool completed;
        bool success;
        void* data;
        size_t data_len;
        int error_code;
        char error_msg[256];
    } AsyncContext;
    
    typedef void (*success_callback)(AsyncContext* ctx, const void* result);
    typedef void (*error_callback)(AsyncContext* ctx, const char* error);
    typedef void (*cleanup_callback)(AsyncContext* ctx);

    typedef struct AsyncOperation {
        AsyncContext* ctx;
        success_callback on_success;
        error_callback on_error;
        cleanup_callback cleanup;
    } AsyncOperation;

    void init_context(AsyncContext* ctx);
    void cleanup_context(AsyncContext* ctx);
    void handle_error(AsyncContext* ctx, const char* error);
    void handle_success(AsyncContext* ctx, const void* result);
    bool wait_for_completion(AsyncContext* ctx, int timeout_ms);

    typedef void (callback_fn)(void *data, char **err);

    typedef int64_t go_ref;

    void FreeGoMem(go_ref go_ref);

    go_ref Supply(go_ref go_ref, char **err);
    go_ref SupplyMany(go_ref *go_refs, int num_go_refs, char **err);

    go_ref NewEventsQueryClient(const char* comet_websocket_url);
    go_ref EventsQueryClientEventsBytes(go_ref selfRef, const char* query);

    go_ref NewBlockQueryClient(char *comet_websocket_url, char **err);

    go_ref NewTxContext(char *tcp_url, char **err);

    go_ref NewBlockClient(go_ref cfg_ref, char **err);

    go_ref NewTxClient(go_ref cfg_ref, char *signing_key_name, char **err);
    go_ref TxClient_SignAndBroadcastAny(AsyncOperation* op, go_ref selfRef, char *msg_any_json);
    go_ref TxClient_SignAndBroadcast(AsyncOperation* op, go_ref selfRef, char *msgTypeUrl, char *msg_bz, int msg_bz_len);
""")

# Load the shared library.
libpoktroll_clients = ffi.dlopen("poktroll_clients")


def check_err(err_ptr: ffi.CData):
    if err_ptr[0] != ffi.NULL:
        raise Exception(ffi.string(err_ptr[0]))


def check_ref(go_ref: go_ref):
    assert go_ref != -1
    assert go_ref != 0


class GoManagedMem:
    """
    A base class for all objects which embed Go-managed memory.

    Attributes:
        go_ref: The Go-managed memory reference (int).
    """

    go_ref: go_ref
    err_ptr: ffi.CData = ffi.new("char **")

    def __init__(self, go_ref: go_ref):
        """
        Constructor for GoManagedMem. Stores the Go-managed memory reference.
        """

        self.go_ref = go_ref

        check_err(self.err_ptr)
        check_ref(go_ref)

    def __del__(self):
        """
        Destructor for GoManagedMem. Frees the Go-managed memory associated with the reference.
        """

        libpoktroll_clients.FreeGoMem(self.go_ref)


class EventsQueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, comet_websocket_url: str):
        go_ref = libpoktroll_clients.NewEventsQueryClient(comet_websocket_url.encode('utf-8'))
        super().__init__(go_ref)

    def EventsBytes(self, query: str) -> go_ref:
        return libpoktroll_clients.EventsQueryClientEventsBytes(self.go_ref, query.encode('utf-8'))


class BlockQueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    self_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, comet_websocket_url: str):
        go_ref = libpoktroll_clients.NewBlockQueryClient(comet_websocket_url.encode('utf-8'),
                                                         self.err_ptr)

        super().__init__(go_ref)


def Supply(go_ref: go_ref) -> go_ref:
    """
    Supplies a Go-managed memory reference to a returned (Go-managed) depinject config.
    :param go_ref: The Go-managed memory reference to supply via depinject.
    :return: The Go-managed memory reference of the resulting depinject config.
    """

    err_ptr = ffi.new("char **")
    cfg_ref = libpoktroll_clients.Supply(go_ref, err_ptr)

    check_err(err_ptr)
    check_ref(cfg_ref)

    return cfg_ref


def SupplyMany(*go_objs: GoManagedMem) -> go_ref:
    """
    Supplies multiple Go-managed memory references to a returned (Go-managed) depinject config.
    :param go_objs: The Go-managed memory objects to supply via depinject.
    :return: The Go-managed memory reference of the resulting depinject config.
    """

    go_refs = [go_obj.go_ref for go_obj in go_objs]
    cgo_refs = ffi.new("go_ref[]", go_refs)
    err_ptr = ffi.new("char **")

    cfg_ref = libpoktroll_clients.SupplyMany(cgo_refs, len(go_objs), err_ptr)

    check_err(err_ptr)
    check_ref(cfg_ref)

    return cfg_ref


class TxContext(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, tcp_url: str):
        """
        Constructor for TxContext.
        :param tcp_url: The gRPC URL for the client to use (e.g. tcp://127.0.0.1:26657).
        """

        go_ref = libpoktroll_clients.NewTxContext(tcp_url.encode('utf-8'), self.err_ptr)
        super().__init__(go_ref)


class BlockClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, cfg_ref: go_ref):
        """
        Constructor for BlockClient.
        :param cfg_ref: A Go-managed memory reference to a depinject config.
        """

        go_ref = libpoktroll_clients.NewBlockClient(cfg_ref, self.err_ptr)
        super().__init__(go_ref)


class TxClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData
    _callback_idx: INTEGRAL = atomic(width=8, atype=INT)
    _callback_fns: Dict[int, Tuple[ffi.CData, ffi.CData, ffi.CData]] = {}

    def __init__(self, cfg_ref: go_ref, signing_key_name: str):
        """
        Constructor for TxClient.
        :param cfg_ref: A Go-managed memory reference to a depinject config.
        """
        go_ref = libpoktroll_clients.NewTxClient(cfg_ref, signing_key_name.encode('utf-8'), self.err_ptr)
        super().__init__(go_ref)

        check_err(self.err_ptr)
        check_ref(go_ref)

    async def SignAndBroadcastAny(self, msg_any_json: str) -> asyncio.Future:
        """
        Signs and broadcasts a transaction.
        :param msg_any_json: The transaction to sign and broadcast.
        :return: Future that completes when the transaction is processed.
        """
        op, future = self._new_async_operation()
        err_ch_ref = libpoktroll_clients.TxClient_SignAndBroadcastAny(
            op,
            self.go_ref,
            msg_any_json.encode('utf-8')
        )

        check_ref(err_ch_ref)
        return await future

    async def SignAndBroadcast(self, msg: Message) -> asyncio.Future:
        """
        Signs and broadcasts a transaction.
        :param msg: The protobuf Message to sign and broadcast.
        :return: Future that completes when the transaction is processed.
        """
        op, future = self._new_async_operation()

        msg_bz = msg.SerializeToString()
        msg_type_url = msg.DESCRIPTOR.full_name.encode('utf-8')

        err_ch_ref = libpoktroll_clients.TxClient_SignAndBroadcast(
            op,
            self.go_ref,
            msg_type_url,
            msg_bz,
            len(msg_bz),
        )

        check_ref(err_ch_ref)
        return await future

    def _new_async_operation(self) -> Tuple[ffi.CData, asyncio.Future]:
        """
        Creates a new AsyncOperation with callbacks and associated Future.
        The callbacks are protected from garbage collection by storing in self._callback_fns.
        """
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        future = loop.create_future()

        # Create AsyncContext
        ctx = ffi.new("AsyncContext *")

        # Define callbacks
        @ffi.callback("void(AsyncContext*, const void*)")
        def success_cb(ctx, result):
            try:
                loop.call_soon_threadsafe(future.set_result, None)
            finally:
                self._cleanup_callbacks()

        @ffi.callback("void(AsyncContext*, const char*)")
        def error_cb(ctx, error):
            try:
                error_str = ffi.string(error).decode('utf-8')
                loop.call_soon_threadsafe(future.set_exception, Exception(error_str))
            finally:
                self._cleanup_callbacks()

        @ffi.callback("void(AsyncContext*)")
        def cleanup_cb(ctx):
            self._cleanup_callbacks()

        # Create AsyncOperation
        op = ffi.new("AsyncOperation *")
        op.ctx = ctx
        op.on_success = success_cb
        op.on_error = error_cb
        op.cleanup = cleanup_cb

        # Store callbacks to protect from garbage collection
        next_callback_idx = self._callback_idx.fetch_inc()
        self._callback_fns[next_callback_idx] = (success_cb, error_cb, cleanup_cb)

        return op, future

    def _cleanup_callbacks(self):
        """
        Clean up stored callbacks.
        """
        self._callback_fns.clear()
