from os import path

from cffi import FFI

# Initialize CFFI
ffi = FFI()

# Load and read the header file contents
thisDirPath = path.dirname(path.abspath(__file__))

# TODO_IN_THIS_COMMIT: comment
ffi.cdef("""
    typedef int64_t GoRef;
    
    GoRef NewEventsQueryClient(const char* comet_websocket_url);
    GoRef EventsQueryClientEventsBytes(GoRef selfRef, const char* query);
""")

# Load the shared object file
sharedObjectPath = path.join(thisDirPath, "..", "ext", "libclients.so")
lib = ffi.dlopen(sharedObjectPath)


class EventsQueryClient:
    selfRef: int  # lib.GoRef

    def __init__(self, comet_websocket_url: str):
        self.selfRef = lib.NewEventsQueryClient(comet_websocket_url.encode('utf-8'))

    def EventsBytes(self, query: str) -> int:  # lib.GoRef:
        return lib.EventsQueryClientEventsBytes(self.selfRef, query.encode('utf-8'))

    def free(self):
        lib.FreeClient(self.selfRef)
