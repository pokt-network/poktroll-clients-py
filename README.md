# `poktroll_clients` - Python Clients Library <!-- omit in toc -->

An [`asyncio`](https://docs.python.org/3/library/asyncio.html) based, cross-platform
Python API which wraps the [`pocket` client packages](https://pkg.go.dev/github.com/pokt-network/pocket@v0.0.10/pkg/client) (formerly, `poktroll`)
(via [`libpoktroll_clients`](https://github.com/pokt-network/libpoktroll-clients)).

## Table of Contents <!-- omit in toc -->

- [Installation](#installation)
  - [PyPI (`pip`)](#pypi-pip)
  - [Source](#source)
    - [1. Clone the repository](#1-clone-the-repository)
    - [2. Download \& install the release wheel](#2-download--install-the-release-wheel)
    - [3. Download and unpack a release tarball](#3-download-and-unpack-a-release-tarball)
- [Getting Started](#getting-started)
  - [Start Pocket Localnet](#start-pocket-localnet)
  - [Usage Examples](#usage-examples)
  - [Local Development Environment Setup](#local-development-environment-setup)

## Installation

> [!IMPORTANT]
> Until some import optimizations are done, the shared libraries are too large to distribute via PyPI. 😢
> In the meantime, the shared libraries MUST be installed separately by following the [libpoktroll-clients README](https://github.com/pokt-network/libpoktroll-clients/blob/main/README.md).

### PyPI (`pip`)

```bash
pip install poktroll_clients
```

### Source

Download and install from source via **any one** of the following (e.g., for version `0.2.0a0.dev1`):

#### 1. Clone the repository

Clone the repository and check out the desired release version tag.

```bash
git clone https://github.com/pokt-network/poktroll-clients-py
git checkout v0.2.0a0.dev1
```

#### 2. Download & install the release wheel

Download and install a release wheel from the [releases page](https://github.com/pokt-network/poktroll-clients-py/releases).

```bash
wget https://github.com/pokt-network/libpoktroll-clients/releases/download/v0.2.0a0/poktroll_clients-0.2.0a0.dev1-py3-none-any.whl
pip install ./poktroll_clients-0.2.0a0.dev1-py3-none-any.whl
```

OR

```bash
pipenv install ./poktroll_clients-0.2.0a0.dev1-py3-none-any.whl
```

#### 3. Download and unpack a release tarball

Download and unpack a release tarball from the [releases page](https://github.com/pokt-network/poktroll-clients-py/releases).

```bash
wget 
pip install ./poktroll_clients-0.2.0a0.dev1.tar.gz
```

OR

```bash
pipenv install ./poktroll_clients-0.2.0a0.dev1.tar.gz
```

## Getting Started

### Start Pocket Localnet

```bash
git clone https://github.com/pokt-network/poktroll
cd poktroll

# Start poktroll localnet
make localnet_up
# Press "space" to open the Tilt web UI

# After the validator service is running (in a separate terminal)
make acc_initialize_pubkeys
```

### Usage Examples

```python
from pprint import pprint
import asyncio
from pocket_clients.proto.pocket.application.tx_pb2 import *
from pocket_clients.proto.pocket.shared.service_pb2 import *
from pocket_clients.proto.cosmos.base.v1beta1.coin_pb2 import *
from pocket_clients import (
  TxClient,
  QueryClient,
)

"""
Signing key name should match the name of a key in the local pocketd keyring
which is authorized to sign for any transactions the tx client will broadcast.
See `pocketd keys -h` for more information.
"""
signing_key_name = "key-name"

"""
Query node RPC URL is the HTTP URL for the pocket RPC endpoint to which query
clients will send requests.
"""
query_node_rpc_url = "http://127.0.0.1:26657"

"""
Tx node RPC URL is the gRPC gateway URL for the pocket RPC endpoint to which the
tx client will connect and broadcast signed transactions. It MUST use the tcp:// scheme.
"""
tx_node_rpc_url = "tcp://127.0.0.1:26657"

tx_client = TxClient(signing_key_name,
                     query_node_rpc_url=query_node_rpc_url,
                     tx_node_rpc_url=tx_node_rpc_url)

query_client = QueryClient(query_node_rpc_url)

app3_addr = "pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex"
gateway1_addr = "pokt15vzxjqklzjtlz7lahe8z2dfe9nm5vxwwmscne4"
gateway2_addr = "pokt15w3fhfyc0lttv7r585e2ncpf6t2kl9uh8rsnyz"


async def main():
  # Application 3 tx client (app3 SHOULD NOT be staked)
  app_tx_client = TxClient("app3",
                           query_node_rpc_url=query_node_rpc_url,
                           tx_node_rpc_url=tx_node_rpc_url)

    # Stake and delegate application 3 to gateways 1 & 2 (in one tx)
    await app_tx_client.sign_and_broadcast(
        MsgStakeApplication(
            address="pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex",
            stake=Coin(denom="upokt", amount="100000000"),
            services=[ApplicationServiceConfig(service_id="anvil")]
        ),
        *[MsgDelegateToGateway(
            app_address=app3_addr,
            gateway_address=gateway_addr,
        ) for gateway_addr in [gateway1_addr, gateway2_addr]],
    )
    
    # Query all applications
    applications = query_client.get_all_applications()
    pprint(applications)

  # Unstake application 3
  await app_tx_client.sign_and_broadcast(
    MsgUnstakeApplication(address=app3_addr),
  )


if __name__ == "__main__":
  asyncio.run(main())
```

### Local Development Environment Setup

```bash
git clone https://github.com/pokt-network/poktroll-clients-py
cd poktroll-clients-py

# Install dependencies
pip install pipenv
pipenv install
pipenv shell

# (optional) Update protobufs ("pull" from buf.build)
buf export buf.build/pokt-network/pocket

# (optional) Re-generate protobufs & fix imports
buf generate && python ./scripts/fix_proto_imports.py

# Install the package in editable mode
pip install -e .

# Run tests (shared library MUST be installed)
pytest
```

This step is optional, but necessary if you intend on developing, and locally integrating, modified versions of the `libpoktroll_clients` shared library.
Otherwise, the steps in the [installation](#installation) section are sufficient to use and develop on the `pocket_clients` python package (i.e., you can skip this step).

```bash
git clone https://github.com/byanchriswhite/libpoktroll_clients
cd libpoktroll_clients

# Build shared library - NOTE: this will take a while until some import optimizations are done.
mkdir build
cd build
cmake ..
make
sudo make install

#OR build and install os-specific package; see libpoktroll_clients/README.md.
```
