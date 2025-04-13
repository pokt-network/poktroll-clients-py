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
  - 1A0BB8623F40D2A9BEAC099A0BAFDCAE3C5D8288 (unstaked)
  - 9B4508816AC8627B364D2EA4FC1B1FEE498D5684 (application)
  - 44892C8AB52396BA016ADDD0221783E3BD29A400 (servicer/supplier)
  - 82510FE41923685BBEE0B4844176AF0AA8EDF198 (unstaked)
  - 5D19E5C0DB2E6B2B860544326CC11F7E847012F7 (application)
  - F30EAED6269EBBA5986DD7ADFA5BBC3C548C6992 (supplier)
<!-- pause -->

Now we can begin claiming!
<!-- end_slide -->

Claiming Morse Accounts via Python
---

A Bob & Alice Story
===
