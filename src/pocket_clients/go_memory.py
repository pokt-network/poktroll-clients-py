from typing import Callable

from cffi import FFIError

from pocket_clients.ffi import ffi, libpocket_clients

go_ref = int
callback_type = Callable[[ffi.CData, ffi.CData], None]


# TODO_IN_THIS_COMMIT: switch to an err_msg[] array

def check_err(err_ptr: ffi.CData) -> None:
    """
    Checks if the error pointer contains an error, and if so, raises an FFIError
    with the error message.
    """
    if err_ptr[0] != ffi.NULL:
        # Get the error message
        err_msg = ffi.string(err_ptr[0]).decode('utf-8')

        # We can't use FreeGoMem directly on err_ptr[0] as it's a char*, not a go_ref
        # The Go code is likely expecting that it's responsible for freeing this memory
        # or that it's stack-allocated

        # Reset the error pointer to prevent double-free attempts
        err_ptr[0] = ffi.NULL

        # Now raise the exception
        raise FFIError(err_msg)


def check_ref(go_ref: go_ref) -> None:
    # TODO_NEXT_libpocket_CLIENT_VERSION: this should be 0.
    if go_ref < 0:
        raise FFIError("unexpected empty go_ref")


class GoManagedMem:
    """
    A base class for all objects which embed Go-managed memory.

    Attributes:
        go_ref: The Go-managed memory reference (int).
    """

    go_ref: go_ref

    def __init__(self, go_ref: go_ref):
        """
        Constructor for GoManagedMem. Stores the Go-managed memory reference.
        """
        # Initialize error pointer if not already initialized by a subclass
        if not hasattr(self, 'err_ptr'):
            self.err_ptr = ffi.new("char **")

        self.go_ref = go_ref

        check_err(self.err_ptr)
        check_ref(go_ref)

    def __del__(self):
        """
        Destructor for GoManagedMem. Frees the Go-managed memory associated with the reference.
        """
        libpocket_clients.FreeGoMem(self.go_ref)
