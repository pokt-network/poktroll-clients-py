import os
from os import path

import pytest

from pocket_clients import TxClient, libpocket_clients, ffi, check_err
from pocket_clients.gas import GasSettings
from pocket_clients.proto.pocket.migration import (new_signed_msg_claim_morse_account,
                                                   new_signed_msg_claim_morse_application,
                                                   new_signed_msg_claim_morse_supplier)
from pocket_clients.proto.pocket.shared.service_pb2 import SupplierServiceConfig, SupplierEndpoint, JSON_RPC, \
    ServiceRevenueShare
from tests.test_tx_client import get_tx_client_deps

project_root = path.abspath(path.join(path.dirname(__file__), ".."))

faucet_addr = "pokt1awtlw5sjmw2f5lgj8ekdkaqezphgz88rdk93sk"
app1_addr = "pokt1mrqt5f7qh8uxs27cjm9t7v9e74a9vvdnq5jva4"


@pytest.mark.asyncio
async def test_morse_migration():
    deps_ref = get_tx_client_deps()
    tx_client = TxClient("faucet", deps_ref, gas_settings=GasSettings(gas_limit=1000000))

    claim_messages = []

    morse_keys_dir = path.join(project_root, "morse_keys")
    with os.scandir(morse_keys_dir) as dir_iterator:
        for key_idx, file in enumerate(dir_iterator):
            if not file.name.startswith(".") and file.is_file() and file.name.endswith(".key"):
                err_ptr = ffi.new("char **")
                morse_export_key_path = file.path.encode('utf-8')
                morse_priv_key_ref = libpocket_clients.LoadMorsePrivateKey(morse_export_key_path, ffi.NULL, err_ptr)
                check_err(err_ptr)

                match key_idx % 3:
                    case 1:
                        msg, c_objects = new_signed_msg_claim_morse_account(
                            shannon_dest_address=faucet_addr,
                            morse_priv_key_ref=morse_priv_key_ref,
                            shannon_signing_address=faucet_addr,
                        )
                        claim_messages.append(msg)
                    case 2:
                        msg, c_objects = new_signed_msg_claim_morse_application(
                            shannon_dest_address=faucet_addr,
                            morse_priv_key_ref=morse_priv_key_ref,
                            service_id="anvil",
                            shannon_signing_address=faucet_addr,
                        )
                        claim_messages.append(msg)
                    case 0:
                        msg, c_objects = new_signed_msg_claim_morse_supplier(
                            shannon_owner_address=faucet_addr,
                            shannon_operator_address=faucet_addr,
                            morse_priv_key_ref=morse_priv_key_ref,
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
                                            address=faucet_addr,
                                            rev_share_percentage=100
                                        )
                                    ]
                                )
                            ],
                            shannon_signing_address=faucet_addr,
                        )
                        claim_messages.append(msg)

    await tx_client.sign_and_broadcast(*claim_messages)
