# Release Process <!-- omit in toc -->

- [Steps](#steps)
  - [Supported OSes / Architectures:](#supported-oses--architectures)
  - [Building `poktroll_clients` python package](#building-poktroll_clients-python-package)
    - [Start a docker container](#start-a-docker-container)
    - [Build the binaries](#build-the-binaries)
    - [Publish to PyPI](#publish-to-pypi)

## Steps

1. cpack macos installer
2. cpack windows installer
3. release libpoktroll_clients
   - github
     - tag
     - installers
     - shared libs
4. release poktroll-clients-py
   - github
     - tag
     - tgzs
     - wheels
     - notes: reference README.md section re: installing shared libs
   - pypi
     - tgzs
     - wheels

### Supported OSes / Architectures:

- OSes
  - Linux
  - MacOS
  - Windows
- Architectures
  - x86_64
  - arm64

### Building `poktroll_clients` python package

#### Start a docker container

TODO_IMPROVE: figure out why `python -m build` seems to do nothing in the pipenv virtualenv.
Using docker as a workaround for isolation between build and host python envs.

```bash
docker run --rm -it -v $(pwd):/poktroll-clients-py python:3.11 bash
```

#### Build the binaries

The following commands will output the build artifacts to the host's `poktroll-clients-py/dist/` directory.

```bash
cd /poktroll-clients-py
pip install pipenv build
pipenv install --system
python -m build

# Check the new files in the dist/ directory
ls dist/
```

#### Publish to PyPI

> [!IMPORTANT]
> Only run this step when you are ready to publish the package to PyPI.

```bash
twine upload dist/*
```
