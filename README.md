# My best python project

[![PyPI](
  https://img.shields.io/pypi/v/my-best-python-project?color=blue
  )](
  https://pypi.org/project/my-best-python-project/
) [![Maintainability](
  https://api.codeclimate.com/v1/badges/e6d94059d1dc7f08d2a4/maintainability
  )](
  https://codeclimate.com/github/eggplants/my-best-python-project/maintainability
) [![Release Package](
  https://github.com/eggplants/my-best-python-project/actions/workflows/release.yml/badge.svg
  )](
  https://github.com/eggplants/my-best-python-project/actions/workflows/release.yml
)

[![pre-commit.ci status](
  https://results.pre-commit.ci/badge/github/eggplants/my-best-python-project/master.svg
  )](
  https://results.pre-commit.ci/latest/github/eggplants/my-best-python-project/master
) [![pages-build-deployment](
  https://github.com/eggplants/my-best-python-project/actions/workflows/pages/pages-build-deployment/badge.svg
  )](
  https://github.com/eggplants/my-best-python-project/actions/workflows/pages/pages-build-deployment
)

This is a sample project.

## Installation

```sh
pip install git+https://github.com/eggplants/my-best-python-project
# or,
pip install my-best-python-project
```

## Usage

### CLI

```shellsession
$ mbpp -h
usage: mbpp [-h] [-o PATH] [--overwrite] [-q] [-V]

This command prints package's version.

optional arguments:
  -h, --help              show this help message and exit
  -o PATH, --output PATH  output to file (default: None)
  --overwrite             overwrite when using `-o` (default: False)
  -q, --quiet             quiet mode (default: False)
  -V, --version           show program's version number and exit

note:
    This package and tool is a sample.

$ mbpp
This package's version is: 0.0.1

$ mbpp -q
0.0.1

$ mbpp -o test.txt
Output: 'test.txt'

$ mbpp -o test.txt
Error: File 'test.txt' exists. To overwrite, use `-o`.

$ mbpp -o test.txt --overwrite
Output: 'test.txt'
```

### Library

To print this package's version:

```python
import my_best_python_project

print(my_best_python_project.__version__)
```

## Development

To setup development environment:

```sh
pip install -e ".[all]"
pre-commit install
```

To run pre-commit hooks manually:

```sh
pre-commit run
# or,
pre-commit run --all-fileso
```

## License

[MIT License](https://github.com/eggplants/my-best-python-project/blob/master/LICENSE)
