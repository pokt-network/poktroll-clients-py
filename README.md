# `poktroll_clients` - Python Clients Library <!-- omit in toc -->

An [`asyncio`](https://docs.python.org/3/library/asyncio.html) based, cross-platform
Python API which wraps the [`poktroll` client packages](https://pkg.go.dev/github.com/pokt-network/poktroll@v0.0.10/pkg/client)
(via [`libpoktroll_clients`](https://github.com/pokt-network/libpoktroll-clients)).

## Table of Contents <!-- omit in toc -->

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Using PyPI (`pip`)](#using-pypi-pip)
  - [From Source](#from-source)
    - [Option 1: Cloning the repository](#option-1-cloning-the-repository)
    - [Option 2. Download \& install the release wheel](#option-2-download--install-the-release-wheel)
    - [Option 3: Download and unpack a release tarball](#option-3-download-and-unpack-a-release-tarball)
    - [Option 4: Build from source](#option-4-build-from-source)
  - [Option 1: LocalNet](#option-1-localnet)
  - [Option 1: Beta TestNet](#option-1-beta-testnet)
  - [Usage Examples](#usage-examples)
- [`poktroll-clients` Development](#poktroll-clients-development)

## Installation

> [!IMPORTANT]
> Until some import optimizations are done, the shared libraries are too large to distribute via PyPI. 😢
>
> In the meantime, the shared libraries MUST be installed separately by following the [libpoktroll-clients README](https://github.com/pokt-network/libpoktroll-clients/blob/main/README.md).

### Prerequisites

1. Install the [poktroll CLI](https://dev.poktroll.com/operate/user_guide/install)
2. If you're using macOS, run `brew install cmake pkg-config`
3. ???

- [libpoktroll-clients](https://github.com/pokt-network/libpoktroll-clients)

### Using PyPI (`pip`)

```bash
pip install poktroll_clients
```

### From Source

Download and install from source via **any single one** of the options outlined
below.

The examples shown are for for version `0.2.0a0.dev1`. Use `git tag --list` to
see all available tags and select the one you want.

#### Option 1: Cloning the repository

Clone the repository and checkout the desired release version tag.

```bash
git clone https://github.com/pokt-network/poktroll-clients-py
git checkout v0.2.0a0.dev1
# TODO_IN_THIS_COMMIT: What is intended to be run here?
pip install . # add -e flag to install in editable mode and reflect local changes
```

#### Option 2. Download & install the release wheel

**TODO_IN_THIS_COMMIT: FIX THE MISSING DYLIB INSTALLATION INSTRUCTIONS.**

Download and install a release wheel from the [releases page](https://github.com/pokt-network/poktroll-clients-py/releases).

```bash
# TODO_IN_THIS_COMMIT: Why is there no .whl file generated/uploaded for v0.2.0a0.dev1? https://github.com/pokt-network/poktroll-clients-py/releases/tag/v0.2.0a0.dev1
wget https://github.com/pokt-network/poktroll-clients-py/releases/download/v0.2.0a0.dev1/poktroll_clients-0.2.0a0.dev1.dev4-py3-none-any.whl
pip install ./poktroll_clients-0.2.0a0.dev1-py3-none-any.whl
```

OR

```bash
pipenv install ./poktroll_clients-0.2.0a0.dev1-py3-none-any.whl
```

#### Option 3: Download and unpack a release tarball

Download and unpack a release tarball from the [releases page](https://github.com/pokt-network/poktroll-clients-py/releases).

```bash
wget https://github.com/pokt-network/poktroll-clients-py/releases/download/v0.2.0a0.dev1/poktroll_clients-0.2.0a0.dev1.tar.gz
pip install ./poktroll_clients-0.2.0a0.dev1.tar.gz
```

OR

```bash
pipenv install ./poktroll_clients-0.2.0a0.dev1.tar.gz
```

#### Option 4: Build from source

Start a docker container and build the binaries following the instructions
from the [release process](./docs/release_process.md):

```bash
docker run --rm -it -v $(pwd):/poktroll-clients-py python:3.11 bash
```

Build the binaries in the docker container:

```bash
cd /poktroll-clients-py
pip install pipenv build
pipenv install --system
python -m build
```

On the host machine, install the generated .whl file:

```bash
# pip install pipenv
# pipenv install
# pipenv shell
pip install ./dist/poktroll_clients-0.2.0a0.dev1-py3-none-any.whl

# (Optional) Check the installed files
pip show -f poktroll-clients

# (Optional) Check that everything is working
python example.py
```

### Option 1: LocalNet

For details on how to run a poktroll localnet
[here](https://dev.poktroll.com/develop/developer_guide/quickstart).

```bash
git clone https://github.com/pokt-network/poktroll
cd poktroll

# Start poktroll localnet
make localnet_up
# Press "space" to open the Tilt web UI

# After the validator service is running (in a separate terminal)
make acc_initialize_pubkeys
```

### Option 1: Beta TestNet

### Usage Examples

```python
from pprint import pprint
import asyncio
from poktroll_clients.proto.poktroll.application.tx_pb2 import *
from poktroll_clients.proto.poktroll.shared.service_pb2 import *
from poktroll_clients.proto.cosmos.base.v1beta1.coin_pb2 import *
from poktroll_clients import (
    TxClient,
    QueryClient,
)

"""
Signing key name should match the name of a key in the local poktrolld keyring
which is authorized to sign for any transactions the tx client will broadcast.
See `poktrolld keys -h` for more information.
"""
signing_key_name = "key-name"

"""
Query node RPC URL is the HTTP URL for the poktroll RPC endpoint to which query
clients will send requests.
"""
# query_node_rpc_url = "http://127.0.0.1:26657"
query_node_rpc_url = "https://shannon-testnet-grove-rpc.beta.poktroll.com"

"""
Tx node RPC URL is the gRPC gateway URL for the poktroll RPC endpoint to which the
tx client will connect and broadcast signed transactions. It MUST use the tcp:// scheme.
"""
# tx_node_rpc_url = "tcp://127.0.0.1:26657"
tx_node_rpc_url = "https://shannon-testnet-grove-grpc.beta.poktroll.com"

tx_client = TxClient(
    signing_key_name,
    query_node_rpc_url=query_node_rpc_url,
    tx_node_rpc_url=tx_node_rpc_url,
)

query_client = QueryClient(query_node_rpc_url)

app3_addr = "pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex"
gateway1_addr = "pokt15vzxjqklzjtlz7lahe8z2dfe9nm5vxwwmscne4"
gateway2_addr = "pokt15w3fhfyc0lttv7r585e2ncpf6t2kl9uh8rsnyz"


async def main():
    # Application 3 tx client (app3 SHOULD NOT be staked)
    app_tx_client = TxClient(
        "app3", query_node_rpc_url=query_node_rpc_url, tx_node_rpc_url=tx_node_rpc_url
    )

    # Stake and delegate application 3 to gateways 1 (in one tx)
    await app_tx_client.sign_and_broadcast(
        MsgStakeApplication(
            address="pokt1lqyu4v88vp8tzc86eaqr4lq8rwhssyn6rfwzex",
            stake=Coin(denom="upokt", amount="100000000"),
            services=[ApplicationServiceConfig(service_id="anvil")],
        ),
        *[
            MsgDelegateToGateway(
                app_address=app3_addr,
                gateway_address=gateway_addr,
            )
            for gateway_addr in [gateway1_addr, gateway2_addr]
        ],
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

## `poktroll-clients` Development

> [!IMPORTANT]
> This section is only intended for developers of the client library, not its users.

Follow the (opinionated) instructions below to prepare your environment for local development.

```bash
git clone https://github.com/pokt-network/poktroll-clients-py
cd poktroll-clients-py

# Build shared library - NOTE: this will take a while until some import optimizations are done.
mkdir build
cd build
cmake ..
make
sudo make install

# Install python env dependencies
pip install pipenv
pipenv install
pipenv shell

# (optional) Update protobufs ("pull" from buf.build)
buf export buf.build/pokt-network/poktroll

# (optional) Re-generate protobufs & fix imports
buf generate && python ./scripts/fix_proto_imports.py

# Install the package in editable mode
pip install -e .

# Run tests (shared library MUST be installed)
pytest
```
