import os
from os import path

from pocket_clients import TxClient, QueryClient, ffi, libpocket_clients, check_err
from pocket_clients.proto.pocket.migration import new_signed_msg_claim_morse_account, \
    new_signed_msg_claim_morse_application, new_signed_msg_claim_morse_supplier
from pocket_clients.proto.pocket.shared.service_pb2 import SupplierServiceConfig, SupplierEndpoint, ServiceRevenueShare, \
    JSON_RPC
from tests.test_tx_client import get_tx_client_deps

project_root = path.abspath(path.join(path.dirname(__file__), "..", ".."))
morse_keys_dir = path.join(project_root, "morse_keys")

def load_morse_key(idx: int, address: str) -> ffi.CData:
    err_ptr = ffi.new("char **")
    morse_export_key_path = path.join(morse_keys_dir, f"{idx}_{address}.key").encode('utf-8')
    morse_priv_key_ref = libpocket_clients.LoadMorsePrivateKey(morse_export_key_path, ffi.NULL,
                                                               err_ptr)
    check_err(err_ptr)
    return morse_priv_key_ref


morse_addresses = []
with os.scandir(morse_keys_dir) as dir_iterator:
    for key_idx, file in enumerate(dir_iterator):
        if not file.name.startswith(".") and file.is_file() and file.name.endswith(".key"):
            morse_addresses.append(file.name[2:-4])

morse_priv_keys = {
    "bob": {
        "unstaked_1": load_morse_key(0, morse_addresses[0]),
        "unstaked_2": load_morse_key(6, morse_addresses[6]),
        "application": load_morse_key(1, morse_addresses[1]),
    },
    "alice": {
        "unstaked_1": load_morse_key(2, morse_addresses[2]),
        "supplier": load_morse_key(3, morse_addresses[3]),
    }
}

morse_src_addrs = {
    "bob": {
        "unstaked_1": morse_addresses[0],
        "unstaked_2": morse_addresses[3],
        "application": morse_addresses[1],
    },
    "alice": {
        "unstaked_1": morse_addresses[6],
        "supplier": morse_addresses[2],
    }
}

shannon_dest_addrs = {
    "bob": {
        "unstaked": "pokt15rpjxjn6vuq78ymmdw2ump8vvvmgg5ap26qrag",
        "application": "pokt1fffmhccye0kj22sr7s0lfv4wg7ys6sma43q6hs",
},
    "alice": {
        "unstaked": "pokt1kz85ph0xwjtus6d8vh56wgpwa8ud2gt4q5fge4",
        "supplier": "pokt1zdxqawdl05dtlzat9w48m02cpapu824fc6hdsd"
    }
}

shannon_signers = {
    "bob": {
        "key_name": "bob_unstaked",
        "address": "pokt15rpjxjn6vuq78ymmdw2ump8vvvmgg5ap26qrag",
    },
    "alice": {
        "key_name": "dave",
        "address": "pokt17uqecvr6mck693ydpznp384kxhqe57strc4vv6",
    }
}

bob_claim_unstaked1_msg, _ = new_signed_msg_claim_morse_account(
    shannon_dest_address=shannon_dest_addrs["bob"]["unstaked"],
    morse_priv_key_ref=morse_priv_keys["bob"]["unstaked_1"],
    shannon_signing_address=shannon_signers["bob"]["address"],
)

bob_claim_unstaked2_msg, _ = new_signed_msg_claim_morse_account(
    shannon_dest_address=shannon_dest_addrs["bob"]["unstaked"],
    morse_priv_key_ref=morse_priv_keys["bob"]["unstaked_2"],
    shannon_signing_address=shannon_signers["bob"]["address"],
)

bob_claim_application_msg, _ = new_signed_msg_claim_morse_application(
    shannon_dest_address=shannon_dest_addrs["bob"]["application"],
    morse_priv_key_ref=morse_priv_keys["bob"]["application"],
    service_id="anvil",
    shannon_signing_address=shannon_signers["bob"]["address"],
)

bob_claim_msgs = [
    bob_claim_unstaked1_msg,
    bob_claim_unstaked2_msg,
    bob_claim_application_msg,
]

alice_claim_unstaked1_msg, _ = new_signed_msg_claim_morse_account(
    shannon_dest_address=shannon_dest_addrs["alice"]["unstaked"],
    morse_priv_key_ref=morse_priv_keys["alice"]["unstaked"],
    shannon_signing_address=shannon_signers["alice"]["address"],
)

alice_claim_supplier_msg, _ = new_signed_msg_claim_morse_supplier(
    shannon_owner_address=shannon_dest_addrs["alice"]["supplier"],
    shannon_operator_address=shannon_dest_addrs["alice"]["supplier"],
    morse_priv_key_ref=morse_priv_keys["alice"]["supplier"],
    supplier_service_configs=[
        SupplierServiceConfig(
            service_id="anvil",
            endpoints=[
                SupplierEndpoint(
                    url="http://relayminer1:8545",
                    rpc_type=JSON_RPC,
                )
            ],
            rev_share=[
                ServiceRevenueShare(
                    address=shannon_dest_addrs["alice"]["supplier"],
                    rev_share_percentage=100
                )
            ]
        )
    ],
    shannon_signing_address=shannon_signers["alice"]["address"],
)

alice_claim_msgs = [
    alice_claim_unstaked1_msg,
    alice_claim_supplier_msg,
]

query_client = QueryClient("http://127.0.0.1:26657")

bob_tx_client = TxClient("bob_unstaked", get_tx_client_deps())
dave_tx_client = TxClient("dave", get_tx_client_deps())
