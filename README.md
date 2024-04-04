# Leet-Code
Developed with python version `~3.12.1`

Repository for leet code solutions and related code.

## setting up environment
```shell
 python -m venv .venv --prompt leet-code
```

```shell
source .venv/bin/activate
```

```shell
python -m pip install -r requirements.txt
```
## setting up notebooks
```shell
python -m ipykernel install --user --name leet-code --display-name leet-code
```

```shell
jupyter notebook
```

## testing
Test linked_list and binary_tree data structure helpers

```shell
make run-tests
```

Additionally, leetcode challenges will be written as `unittest.TestCase` class and should be run as tests

## black
run `black` on `leet_code/*` code
```shell
make clean-leet-codes
```

run `black` on `tests/` code
```shell
make clean-tests
```

## github
To clean up all __local__ github branches besides main
```shell
make clean-repos
```