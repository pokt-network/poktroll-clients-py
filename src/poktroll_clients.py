from os import path

from cffi import FFI

GoRef = int

# Initialize CFFI
ffi = FFI()

# Load and read the header file contents
thisDirPath = path.dirname(path.abspath(__file__))

# TODO_IN_THIS_COMMIT: comment
# TODO_IN_THIS_COMMIT: refactor into multiple cdefs and move to appropriate files.
ffi.cdef("""
    typedef int64_t GoRef;
    
    void FreeGoMem(GoRef go_ref);
    
    GoRef Supply(GoRef go_ref, char **err);
    GoRef SupplyMany(GoRef *go_refs, int num_go_refs, char **err);
    
    GoRef NewEventsQueryClient(const char* comet_websocket_url);
    GoRef EventsQueryClientEventsBytes(GoRef selfRef, const char* query);
    
    GoRef NewBlockQueryClient(char *comet_websocket_url, char **err);
    
    GoRef NewTxContext(char *tcp_url, char **err);
    
    GoRef NewBlockClient(GoRef cfg_ref, char **err);
    
    GoRef NewTxClient(GoRef cfg_ref, char *signing_key_name, char **err);
    GoRef SignAndBroadcast(GoRef selfRef, char *msg_any_json, char **err);
""")

# Load the shared object file
sharedObjectPath = path.join(thisDirPath, "..", "ext", "libclients.so")
lib = ffi.dlopen(sharedObjectPath)


def check_err(err_ptr: ffi.CData):
    if err_ptr[0] != ffi.NULL:
        raise Exception(ffi.string(err_ptr[0]))


def check_ref(go_ref: GoRef):
    assert go_ref != -1
    assert go_ref != 0


class GoManagedMem:
    """
    A base class for all objects which embed Go-managed memory.

    Attributes:
        go_ref: The Go-managed memory reference (int).
    """

    go_ref: GoRef
    err_ptr: ffi.CData = ffi.new("char **")

    def __init__(self, go_ref: GoRef):
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

        lib.FreeGoMem(self.go_ref)


class EventsQueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: GoRef
    err_ptr: ffi.CData

    def __init__(self, comet_websocket_url: str):
        go_ref = lib.NewEventsQueryClient(comet_websocket_url.encode('utf-8'))
        super().__init__(go_ref)

    def EventsBytes(self, query: str) -> GoRef:
        return lib.EventsQueryClientEventsBytes(self.go_ref, query.encode('utf-8'))


class BlockQueryClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    self_ref: GoRef
    err_ptr: ffi.CData

    def __init__(self, comet_websocket_url: str):
        go_ref = lib.NewBlockQueryClient(comet_websocket_url.encode('utf-8'),
                                         self.err_ptr)

        super().__init__(go_ref)


def Supply(go_ref: GoRef) -> GoRef:
    """
    Supplies a Go-managed memory reference to a returned (Go-managed) depinject config.
    :param go_ref: The Go-managed memory reference to supply via depinject.
    :return: The Go-managed memory reference of the resulting depinject config.
    """

    err_ptr = ffi.new("char **")
    cfg_ref = lib.Supply(go_ref, err_ptr)

    check_err(err_ptr)
    check_ref(cfg_ref)

    return cfg_ref


def SupplyMany(*go_objs: GoManagedMem) -> GoRef:
    """
    Supplies multiple Go-managed memory references to a returned (Go-managed) depinject config.
    :param go_objs: The Go-managed memory objects to supply via depinject.
    :return: The Go-managed memory reference of the resulting depinject config.
    """

    go_refs = [go_obj.go_ref for go_obj in go_objs]
    cgo_refs = ffi.new("GoRef[]", go_refs)
    err_ptr = ffi.new("char **")

    cfg_ref = lib.SupplyMany(cgo_refs, len(go_objs), err_ptr)

    check_err(err_ptr)
    check_ref(cfg_ref)

    return cfg_ref


class TxContext(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: GoRef
    err_ptr: ffi.CData

    def __init__(self, tcp_url: str):
        """
        Constructor for TxContext.
        :param tcp_url: The gRPC URL for the client to use (e.g. tcp://127.0.0.1:26657).
        """

        go_ref = lib.NewTxContext(tcp_url.encode('utf-8'), self.err_ptr)
        super().__init__(go_ref)


class BlockClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: GoRef
    err_ptr: ffi.CData

    def __init__(self, cfg_ref: GoRef):
        """
        Constructor for BlockClient.
        :param cfg_ref: A Go-managed memory reference to a depinject config.
        """

        go_ref = lib.NewBlockClient(cfg_ref, self.err_ptr)
        super().__init__(go_ref)


class TxClient(GoManagedMem):
    """
    TODO_IN_THIS_COMMIT: comment
    """

    go_ref: GoRef
    err_ptr: ffi.CData

    def __init__(self, cfg_ref: GoRef, signing_key_name: str):
        """
        Constructor for TxClient.
        :param cfg_ref: A Go-managed memory reference to a depinject config.
        """

        go_ref = lib.NewTxClient(cfg_ref, signing_key_name.encode('utf-8'), self.err_ptr)
        super().__init__(go_ref)

        check_err(self.err_ptr)
        check_ref(go_ref)

    def SignAndBroadcast(self, msg_any_json: str) -> GoRef:
        """
        Signs and broadcasts a transaction.
        :param msg_any_json: The transaction to sign and broadcast.
        :return: The Go-managed memory reference of the err channel which is
        notified if the resulting transaction fails the CheckTX ABCI++ method.
        """

        err_ch_ref =  lib.SignAndBroadcast(self.go_ref, msg_any_json.encode('utf-8'), self.err_ptr)

        check_err(self.err_ptr)
        check_ref(err_ch_ref)
