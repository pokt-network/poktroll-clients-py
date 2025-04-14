from pocket_clients import TxClient, QueryClient, ffi, libpocket_clients, check_err
from pocket_clients.proto.pocket.migration import new_signed_msg_claim_morse_account, new_signed_msg_claim_morse_application, new_signed_msg_claim_morse_supplier
from pocket_clients.proto.pocket.shared.service_pb2 import SupplierServiceConfig, SupplierEndpoint, ServiceRevenueShare, JSON_RPC

from demo_prez.keys import load_morse_key, morse_addresses
from tests.test_tx_client import get_tx_client_deps

# Initialize a client for querying onchain data.
query_client = QueryClient("http://127.0.0.1:26657")

# Initialize clients for signing & broadcasting Morse claim transactions.
# NOTE: Simone is signing on behalf of Alice to demonstrate custodial claiming.
bob_tx_client = TxClient("bob_unstaked", get_tx_client_deps())
simone_tx_client = TxClient("simone", get_tx_client_deps())

# A dictionary of Morse private keys, grouped by user and account.
morse_priv_keys = {
    "bob": {
        "unstaked_1": load_morse_key(0, morse_addresses[0]),
        "unstaked_2": load_morse_key(3, morse_addresses[3]),
        "application": load_morse_key(1, morse_addresses[1]),
    },
    "alice": {
        "unstaked": load_morse_key(6, morse_addresses[6]),
        "supplier": load_morse_key(2, morse_addresses[2]),
    }
}

# A dictionary of Morse source addresses, grouped by user.
# Each user can have multiple Morse accounts, which map to distinct Morse addresses.
morse_src_addrs = {
    "bob": {
        "unstaked_1": morse_addresses[0],
        "unstaked_2": morse_addresses[3],
        "application": morse_addresses[1],
    },
    "alice": {
        "unstaked": morse_addresses[6],
        "supplier": morse_addresses[2],
    }
}

# A dictionary of Shannon destination addresses, grouped by user.
# Each user may have multiple Shannon accounts (key names), which
# map to distinct Shannon addresses.
shannon_dest_addrs = {
    "bob": {
        "unstaked": "pokt15rpjxjn6vuq78ymmdw2ump8vvvmgg5ap26qrag",
        "application": "pokt1fffmhccye0kj22sr7s0lfv4wg7ys6sma43q6hs",
},
    "alice": {
        "supplier_operator": "pokt1hkcslgef4l88xncjq592v04q6gu06puur48zaw",
        "supplier_owner": "pokt1257n0hnn84g08p4rmf9q0p4nztnlukqpvaydng"
    }
}

# A dictionary of Shannon key names/addrs to be used for signing the Morse claims.
# Each Morse account/actor claim transaction will use a single Shannon signing account.
# In Alice's case, the Simone user will be responsible for signing to demonstrate
# custodial account/actor claiming.
shannon_signers = {
    "bob": {
        "key_name": "bob_unstaked",
        "address": "pokt15rpjxjn6vuq78ymmdw2ump8vvvmgg5ap26qrag",
    },
    "alice": {
        "key_name": "simone",
        "address": "pokt17uqecvr6mck693ydpznp384kxhqe57strc4vv6",
    }
}

# Bob's account/actor claim messages.
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
# ---

# Alice's Morse account/actor claim messages.
alice_claim_unstaked_as_supplier_owner_msg, _ = new_signed_msg_claim_morse_account(
    shannon_dest_address=shannon_dest_addrs["alice"]["supplier_owner"],
    morse_priv_key_ref=morse_priv_keys["alice"]["unstaked"],
    shannon_signing_address=shannon_signers["alice"]["address"],
)

alice_claim_supplier_msg, _ = new_signed_msg_claim_morse_supplier(
    shannon_owner_address=shannon_dest_addrs["alice"]["supplier_owner"],
    shannon_operator_address=shannon_dest_addrs["alice"]["supplier_operator"],
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
                    address=shannon_dest_addrs["alice"]["supplier_owner"],
                    rev_share_percentage=100
                )
            ]
        )
    ],
    shannon_signing_address=shannon_signers["alice"]["address"],
)

alice_claim_msgs = [
    alice_claim_unstaked_as_supplier_owner_msg,
    alice_claim_supplier_msg,
]
# ---
