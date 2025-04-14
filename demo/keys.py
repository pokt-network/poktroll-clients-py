import os
from os import path

from pocket_clients import check_err
from pocket_clients.ffi import ffi, libpocket_clients

project_root = path.abspath(path.join(path.dirname(__file__), ".."))
morse_keys_dir = path.join(project_root, "morse_keys")

def load_morse_key(idx: int, address: str) -> ffi.CData:
    err_ptr = ffi.new("char **")
    morse_export_key_path = path.join(morse_keys_dir, f"{idx}_{address}.key").encode('utf-8')
    morse_priv_key_ref = libpocket_clients.LoadMorsePrivateKey(morse_export_key_path, ffi.NULL,
                                                               err_ptr)
    check_err(err_ptr)
    return morse_priv_key_ref

morse_addresses = []
entries = list(os.scandir(morse_keys_dir))
entries.sort(key=lambda entry: entry.name)

for key_idx, file in enumerate(entries):
    if not file.name.startswith(".") and file.is_file() and file.name.endswith(".key"):
        morse_addresses.append(file.name[2:-4])

