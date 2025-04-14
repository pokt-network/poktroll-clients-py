Claiming Morse Accounts via Python
---

While we wait for LocalNet to finish comint up, let's take a look at the demo code we'll be working with...
<!-- pause -->

LocalNet's up - Let's go!
<!-- pause -->

This demonstration will be interactive, using `ipython` to interact with pocket network (Shannon LocalNet) in real-time.
<!-- pause -->

We're starting with a "fresh" LocalNet; i.e., there should be no staked actors nor Morse claimable accounts onchain.

<!-- pause -->
- List existing staked applications...
<!-- pause -->
...None

<!-- pause -->
- List existing staked suppliers...
<!-- pause -->
...None

<!-- pause -->
- List imported Morse claimable accounts...
<!-- pause -->
...None

<!-- end_slide -->

Claiming Morse Accounts via Python
---

Let's import some Morse claimable accounts from a valid `MorseAccountState` that includes accounts for which we have private keys, such that we may claim them.
<!-- pause -->

- Import - Done!
<!-- pause -->

Let's list the Morse claimable accounts again to make sure we see our accounts...
<!-- pause -->

- Success!
  - 1A0BB8623F40D2A9BEAC099A0BAFDCAE3C5D8288
  - 9B4508816AC8627B364D2EA4FC1B1FEE498D5684
  - 44892C8AB52396BA016ADDD0221783E3BD29A400
  - 82510FE41923685BBEE0B4844176AF0AA8EDF198
  - 5D19E5C0DB2E6B2B860544326CC11F7E847012F7
  - F30EAED6269EBBA5986DD7ADFA5BBC3C548C6992
  - 46F75BAEC96D423CFE3C88ADF2593B1FFAE3DBB7
<!-- pause -->

Now we can begin claiming!
<!-- end_slide -->

Claiming Morse Accounts via Python
---

```
Morse account ───── Claim Tx ───── Shannon account
```

<!-- pause -->

A Bob & Alice Story
===

<!-- end_slide -->

Claiming Morse Accounts via Python
---

```
Morse account ───── Claim Tx ───── Shannon account
```

Bob
===

Bob has 3 Morse accounts, 2 unstaked accounts, and 1 staked application.
Bob wants to claim his 2 unstaked accounts to a single Shannon destination account (combining balances), and claim his application account separately.
Bob can combine all his claim messages into a single transaction, and sign it with either Shannon destination account.

```
                    (1 Tx / 3 Msgs)
unstaked_1 ──┬── Claim Unstaked Balances ─── unstaked
unstaked_2 ──┘                        
unstaked_2 ─────── Claim Application ─────── application
```

<!-- pause -->

Resulting in the following:

| Morse Acct. | Morse Source Address                     |
|-------------|------------------------------------------|
| unstaked_1  | 1A0BB8623F40D2A9BEAC099A0BAFDCAE3C5D8288 |
| unstaked_2  | 82510FE41923685BBEE0B4844176AF0AA8EDF198 |
| application | 9B4508816AC8627B364D2EA4FC1B1FEE498D5684 |


| Morse Acct. | Shannon Dest. Address           | Signer          |
|-------------|---------------------------------|-----------------|
| unstaked_1  | pokt15rpjxjn6vuq78ymmdw2ump8... | bob_unstaked    |
| unstaked_2  | pokt15rpjxjn6vuq78ymmdw2ump8... | bob_unstaked    |
| application | pokt1fffmhccye0kj22sr7s0lfv4... | bob_application |

<!-- end_slide -->

Claiming Morse Accounts via Python
---

```
Morse account ───── Claim Tx ───── Shannon account
```

A Bob & Alice Story
===

<!-- end_slide -->

Claiming Morse Accounts via Python
---

```
Morse account ───── Claim Tx ───── Shannon account
```

Alice
===

Alice has 2 Morse accounts, an unstaked account, and a staked servicer/supplier.
Alice wants to migrate her Morse servicer to a Shannon supplier (owner), but she wants to migrate her unstaked account to be the Supplier's operator account
(i.e. operator signs claims/proofs & owner receives rewards).
Similarly, Alice can combine both claim messages into a single transaction, and sign it with either Shannon account.
Furthermore, Simone will be doing the claiming on behalf of Alice, since her accounts are custodial and Simone is in possession of the corresponding Morse private keys.

```
unstaked ──┬──────────── Claim Both ────────── supplier
servicer ──┘  (unstaked -> supplier owner)
              (servicer -> supplier operator)
```

<!-- pause -->

Resulting in the following:

| Morse Acct. | Morse Source Address                     |
|-------------|------------------------------------------|
| unstaked    | 46F75BAEC96D423CFE3C88ADF2593B1FFAE3DBB7 |
| servicer    | 46F75BAEC96D423CFE3C88ADF2593B1FFAE3DBB7 |

| Morse Acct. | Shannon Dest. Address           | Signer |
|-------------|---------------------------------|--------|
| unstaked    | pokt1hkcslgef4l88xncjq592v04... | simone |
| servicer    | pokt1257n0hnn84g08p4rmf9q0p4... | simone |

<!-- end_slide -->
