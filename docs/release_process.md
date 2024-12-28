# Release Process

### Steps

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

```bash
# TODO_IMPROVE: figure out why `python -m build` seems to do nothing in the pipenv virtualenv.
# Using docker as a workaround for isolation between build and host python envs.

docker run --rm -it -v $(pwd):/poktroll-clients-py python:3.11 bash
# Inside docker container:
cd /poktroll-clients-py
pip install pipenv build
pipenv install --system
python -m build
# Build output will be in `poktroll-clients-py/dist/` on the host.

# Publish to PyPI
twine upload dist/*
```
