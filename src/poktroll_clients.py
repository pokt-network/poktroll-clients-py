from os import path

from cffi import FFI

GoRef = int

# Initialize CFFI
ffi = FFI()

# Load and read the header file contents
thisDirPath = path.dirname(path.abspath(__file__))

# TODO_IN_THIS_COMMIT: comment
ffi.cdef("""
    typedef int64_t GoRef;
    
    GoRef NewEventsQueryClient(const char* comet_websocket_url);
    GoRef EventsQueryClientEventsBytes(GoRef selfRef, const char* query);
    
    GoRef NewBlockQueryClient(char *comet_websocket_url, char **err);
""")

# Load the shared object file
sharedObjectPath = path.join(thisDirPath, "..", "ext", "libclients.so")
lib = ffi.dlopen(sharedObjectPath)


class EventsQueryClient:
    self_ref: GoRef

    def __init__(self, comet_websocket_url: str):
        self.self_ref = lib.NewEventsQueryClient(comet_websocket_url.encode('utf-8'))

    def EventsBytes(self, query: str) -> GoRef:
        return lib.EventsQueryClientEventsBytes(self.self_ref, query.encode('utf-8'))

    def free(self):
        lib.FreeClient(self.self_ref)

class BlockQueryClient:
    self_ref: GoRef
    err_ptr: ffi.CData

    def __init__(self, comet_websocket_url: str):
        self.err_ptr = ffi.new("char **")
        self.self_ref = lib.NewBlockQueryClient(
            comet_websocket_url.encode('utf-8'),
            self.err_ptr)

        if self.err_ptr[0] != ffi.NULL:
            raise Exception(ffi.string(self.err_ptr[0]))
