from pocket_clients import QueryClient

fixture_morse_account_addresses = (
    "1A0BB8623F40D2A9BEAC099A0BAFDCAE3C5D8288",
    "9B4508816AC8627B364D2EA4FC1B1FEE498D5684",
    "44892C8AB52396BA016ADDD0221783E3BD29A400",
    "82510FE41923685BBEE0B4844176AF0AA8EDF198",
    "5D19E5C0DB2E6B2B860544326CC11F7E847012F7",
    "F30EAED6269EBBA5986DD7ADFA5BBC3C548C6992",
    "46F75BAEC96D423CFE3C88ADF2593B1FFAE3DBB7",
    "E1641A82AD28F123B9076B6D6A1B5AF5DD2932E0",
    "5EC8FB470400FD215AA63304FD1DA45750AD1385",
    "5EC8FB470400FD215AA63304FD1DA45750AD1385"
)

def test_query_morse_claimable_accounts():
    query_client = QueryClient("http://127.0.0.1:26657")

    migration_params = query_client.get_migration_params()
    assert migration_params.waive_morse_claim_gas_fees == True

    all_morse_accounts = query_client.get_morse_claimable_accounts()
    assert all_morse_accounts is not None

    for morse_address in fixture_morse_account_addresses:
        assert morse_address in [acct.morse_src_address for acct in all_morse_accounts]

        morse_account = query_client.get_morse_claimable_account(morse_address)
        assert morse_account is not None
