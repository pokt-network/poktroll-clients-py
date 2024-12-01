import asyncio
import importlib
from concurrent.futures import Future
from os import path
from typing import Union

from google.protobuf.message import Message

from cffi import FFI

go_ref = int

# Initialize CFFI
ffi = FFI()

# Load and read the header file contents
thisDirPath = path.dirname(path.abspath(__file__))

# ffi.cdef("""""")

ffi.cdef("""
    typedef void* (*callback_type)(void*, char**);
    void *test_callback(void *data, char **err);
    void register_python_callback(callback_type py_cb, callback_type *out_c_cb);
    void *handle_callback(void *data, char **err);
""")

ffi.set_source(
    "callbacks",
    """
    #include <Python.h>
    #include <stdio.h>

    typedef void* (*callback_type)(void*, char**);

    void *test_callback(void *data, char **err) {
        printf("test_callback called\\n");
        printf("data: %p\\n", data);
        printf("err: %p\\n", err);
        return data;    
    }

    static callback_type current_py_callback = NULL;

    void *handle_callback(void *data, char **err) {
        if (current_py_callback) {
            PyGILState_STATE gstate = PyGILState_Ensure();
            void *result = current_py_callback(data, err);
            PyGILState_Release(gstate);
            return result;
        }
        return NULL;
    }

    void register_python_callback(callback_type py_cb, callback_type *out_c_cb) {
        current_py_callback = py_cb;
        *out_c_cb = handle_callback;
    }
    """,
    libraries=['python3']
)
# # Compile if the extension module doesn't exist
# if not path.exists(ffi.modulefilename):
#     ffi.compile()

# TODO_IN_THIS_COMMIT: refactor
# Check if the module is already compiled
# module_name = "callbacks"
# spec = importlib.util.find_spec(module_name)
# print(f">>> spec: {spec}")
# if spec is None:
    # Module doesn't exist, compile it
# TODO_IN_THIS_COMMIT: only bulid if needed... how to know?
ffi.compile(tmpdir="build", target="callbacks")

libcallbacks = ffi.dlopen(path.join(thisDirPath, "..", "build", "callbacks"))

# TODO_IN_THIS_COMMIT: comment
# TODO_IN_THIS_COMMIT: refactor into multiple cdefs and move to appropriate files.
ffi.cdef("""
    typedef void *(callback_fn)(void *data, char **err);
    
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
    go_ref TxClient_SignAndBroadcastAny(go_ref selfRef, char *msg_any_json, char **err);
    go_ref TxClient_SignAndBroadcast(go_ref selfRef, char *msg_bz, int msg_bz_len, char *msgTypeUrl, callback_fn cb, char **err);
""")

# Load the shared object file
sharedObjectPath = path.join(thisDirPath, "..", "ext", "libclients.so")
libclients = ffi.dlopen(sharedObjectPath)


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

        libclients.FreeGoMem(self.go_ref)


class EventsQueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, comet_websocket_url: str):
        go_ref = libclients.NewEventsQueryClient(comet_websocket_url.encode('utf-8'))
        super().__init__(go_ref)

    def EventsBytes(self, query: str) -> go_ref:
        return libclients.EventsQueryClientEventsBytes(self.go_ref, query.encode('utf-8'))


class BlockQueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    self_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, comet_websocket_url: str):
        go_ref = libclients.NewBlockQueryClient(comet_websocket_url.encode('utf-8'),
                                                self.err_ptr)

        super().__init__(go_ref)


def Supply(go_ref: go_ref) -> go_ref:
    """
    Supplies a Go-managed memory reference to a returned (Go-managed) depinject config.
    :param go_ref: The Go-managed memory reference to supply via depinject.
    :return: The Go-managed memory reference of the resulting depinject config.
    """

    err_ptr = ffi.new("char **")
    cfg_ref = libclients.Supply(go_ref, err_ptr)

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

    cfg_ref = libclients.SupplyMany(cgo_refs, len(go_objs), err_ptr)

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

        go_ref = libclients.NewTxContext(tcp_url.encode('utf-8'), self.err_ptr)
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

        go_ref = libclients.NewBlockClient(cfg_ref, self.err_ptr)
        super().__init__(go_ref)


class TxClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: go_ref
    err_ptr: ffi.CData

    def __init__(self, cfg_ref: go_ref, signing_key_name: str):
        """
        Constructor for TxClient.
        :param cfg_ref: A Go-managed memory reference to a depinject config.
        """

        go_ref = libclients.NewTxClient(cfg_ref, signing_key_name.encode('utf-8'), self.err_ptr)
        super().__init__(go_ref)

        check_err(self.err_ptr)
        check_ref(go_ref)

    def SignAndBroadcastAny(self, msg_any_json: str) -> go_ref:
        """
        Signs and broadcasts a transaction.
        :param msg_any_json: The transaction to sign and broadcast.
        :return: The Go-managed memory reference of the err channel which is
        notified if the resulting transaction fails the CheckTX ABCI++ method.
        """

        err_ch_ref = libclients.TxClient_SignAndBroadcastAny(self.go_ref, msg_any_json.encode('utf-8'), self.err_ptr)

        check_err(self.err_ptr)
        check_ref(err_ch_ref)

    # async def SignAndBroadcast(self, msg: Message) -> Union[Future, asyncio.Future]:
    # async def SignAndBroadcast(self, msg: Message) -> asyncio.Future:
    def SignAndBroadcast(self, msg: Message) -> Future:
        """
        Signs and broadcasts a transaction.
        :param msg: The protobuf Message to sign and broadcast.
        // TODO_IN_THIS_COMMIT: update...
        :return: The Go-managed memory reference of the err channel which is
        notified if the resulting transaction fails the CheckTX ABCI++ method.
        """

        # try:
        # loop = asyncio.get_running_loop()
        # future: Future = loop.create_future()
        # is_asyncio = True
        # except RuntimeError:
        future = Future()
        #     is_asyncio = False

        @ffi.callback("void*(void*, char**)")
        def py_callback(data: ffi.CData, err_ptr: ffi.CData) -> ffi.CData:
            # if is_asyncio:
            # loop.call_soon_threadsafe(future.set_result, data, err_ptr)
            # else:
            check_err(err_ptr)

            future.set_result(data)
            return data

        # c_callback = ffi.new("void*(void*, char**)")
        c_callback = ffi.new("callback_fn *[0]")
        self._callback_fn = c_callback
        self._callback_fn2 = py_callback
        libcallbacks.register_python_callback(py_callback, c_callback)

        msg_bz = msg.SerializeToString()
        msg_type_url = msg.DESCRIPTOR.full_name.encode('utf-8')
        c_msg_bz = ffi.new("uint8_t[]", msg_bz)
        err_ch_ref = libclients.TxClient_SignAndBroadcast(self.go_ref,
                                                          c_msg_bz,
                                                          len(msg_bz),
                                                          msg_type_url,
                                                          py_callback,
                                                          # c_callback,
                                                          # libcallbacks.test_callback,
                                                          # libcallbacks.handle_callback,
                                                          self.err_ptr)

        check_err(self.err_ptr)
        check_ref(err_ch_ref)

        return future
