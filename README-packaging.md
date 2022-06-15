# How to build and publish a python package

_See https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives_

## Pre-checking

```shell
python3 -m pip install --upgrade build
pip3 install -U pytest
python3 -m pip install --upgrade twine
```

## Build and install locally

```shell
python3 -m build
python3 -m pip install dist/xxx.whl
```

Run test suites with :

```shell
python3 -m pytest
```

## Publish on pypi

Display the token so that a copy/paste is prepared. Then use the login `__token__`, and paste the token as the password.

```shell
python3 -m twine upload --repository pypi dist/*
```
