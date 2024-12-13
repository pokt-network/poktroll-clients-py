# `poktroll_clients` - Python Clients Library

An [`asyncio`](https://docs.python.org/3/library/asyncio.html) based Python API which wraps the [`poktroll` client packages](https://pkg.go.dev/github.com/pokt-network/poktroll@v0.0.10/pkg/client) (via [`libpoktroll_clients`](https://github.com/bryanchriswhite/libpoktroll-clients)).

## Table of Contents <!-- omit in toc -->

- [Installation](#installation)
  - [PyPI (pip)](#pypi-pip)
  - [Source](#source)
- [Getting started (development environment)](#getting-started-development-environment)
  - [Start poktroll localnet](#start-poktroll-localnet)
  - [Build and install `libpoktroll_clients` shared library & headers](#build-and-install-libpoktroll_clients-shared-library--headers)
  - [Poktroll-clients-py development environment setup](#poktroll-clients-py-development-environment-setup)

## Installation

### PyPI (`pip`)

**NOTE:** Until some import optimizations are done, the shared libraries are too large to distribute via PyPI. 😢
In the meantime, the shared libraries can be installed separately by following the [libpoktroll-clients README](https://github.com/bryanchriswhite/libpoktroll-clients/blob/main/README.md).

```bash
pip install poktroll_clients
```

### Source

Download and install from source via **any one** of the following (e.g., for version `0.1.0a1`):
1. Clone the repository and check out the desired release version tag.
    ```bash
    git clone https://github.com/bryanchriswhite/poktroll-clients-py
    git checkout v0.1.0a1
    ```
2. Download and install a release wheel from the [releases page](https://github.com/bryanchriswhite/poktroll-clients-py/releases).
    ```bash
    wget https://github.com/bryanchriswhite/poktroll-clients-py/releases/download/poktrollv0.1.0a1/poktroll_clients-0.1.0a1-py3-none-any.whl
    pip install ./poktroll_clients-0.1.0a1-py3-none-any.whl
    # OR
    pipenv install ./poktroll_clients-0.1.0a1-py3-none-any.whl
    ```
3. Download and unpack a release tarball from the [releases page](https://github.com/bryanchriswhite/poktroll-clients-py/releases).
    ```bash
    wget https://github.com/bryanchriswhite/poktroll-clients-py/releases/download/v0.1.0a1/poktroll_clients-0.1.0a1.tar.gz
    pip install ./poktroll_clients-0.1.0a1.tar.gz
    # OR
    pipenv install ./poktroll_clients-0.1.0a1.tar.gz
    ```

## Getting started (development environment)

### Start poktroll localnet
```bash
git clone https://github.com/pokt-network/poktroll
cd poktroll

# Start poktroll localnet
make localnet_up
```

### Build and install `libpoktroll_clients` shared library & headers

This step is optional, but necessary if you intend on developing, and locally integrating, modified versions of the `libpoktroll_clients` shared library.
Otherwise, the steps in the [installation](#installation) section are sufficient to use and develop on the `poktroll_clients` python package (i.e., you can skip this step).

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

### Poktroll-clients-py development environment setup
```bash
git clone https://github.com/bryanchriswhite/poktroll-clients-py
cd poktroll-clients-py

# Install dependencies
pip install pipenv
pipenv install
pipenv shell

# (optional) Update protobufs ("pull" from buf.build)
buf export buf.build/pokt-network/poktroll

# (optional) Re-generate protobufs & fix imports
buf generate && python ./scripts/fix_proto_imports.py

# Install the package in editable mode
pip install -e .

# Run tests
pytest
```