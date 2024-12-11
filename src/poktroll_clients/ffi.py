from os import path
from typing import Callable

from cffi import FFI

# Initialize CFFI
ffi = FFI()

# TODO_IN_THIS_COMMIT: comment
callback_type = Callable[[ffi.CData, ffi.CData], None]

# Load and read the header file contents
thisDirPath = path.dirname(path.abspath(__file__))

# TODO_IMPROVE: Extract docstring to an appropriately named file.
# DEV_NOTE: ffi.cdef MUST NOT depend on any pre-processing (e.g. macros, defs, etc.).

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

    typedef struct {
        uint8_t* type_url;
        size_t type_url_length;
        uint8_t* data;
        size_t data_length;
    } serialized_proto;

    typedef struct {
        serialized_proto* messages;
        size_t num_messages;
    } proto_message_array;

    go_ref NewEventsQueryClient(const char* comet_websocket_url);
    go_ref EventsQueryClientEventsBytes(go_ref selfRef, const char* query);

    go_ref NewBlockQueryClient(char *comet_websocket_url, char **err);

    go_ref NewTxContext(char *tcp_url, char **err);

    go_ref NewBlockClient(go_ref cfg_ref, char **err);

    go_ref NewTxClient(go_ref cfg_ref, char *signing_key_name, char **err);
    go_ref TxClient_SignAndBroadcast(AsyncOperation* op, go_ref self_ref, serialized_proto *msg);
    go_ref TxClient_SignAndBroadcastMany(AsyncOperation* op, go_ref self_ref, proto_message_array *msgs);
""")

# Load the shared library.
libpoktroll_clients = ffi.dlopen("poktroll_clients")
