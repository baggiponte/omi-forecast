<div align="center">

# 🏠 OMI Forecast

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![cookiecutter chef](https://img.shields.io/badge/cookiecutter-chef-D4AA00?logo=cookiecutter&logoColor=fff)](https://github.com/baggiponte/chef)
<br>
[![code style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![imports isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)
[![checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy.readthedocs.io/en/stable/)
[![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
<br>
[![documentation mkdocs](https://img.shields.io/badge/documentation-mkdocs-0094F5)](https://www.mkdocs.org/)
[![docstyle google](https://img.shields.io/badge/%20style-google-459db9.svg)](https://numpydoc.readthedocs.io/en/latest/format.html)

</div>

## ⚡ Features

`omi-forecast` is a package to forecast OMI house prices.

## 📦 How to install

`omi-forecast` can be installed with any package manager of your choice, though we use [`pdm`](https://pdm.fming.dev/latest/) for development.

```bash
pdm add omi-forecast
```

## 🤗 Contributing

### Development

1. Install `pdm` and [`just`](https://github.com/casey/just#installation).

2. Clone the repository:

```bash
# using github cli
gh repo clone baggiponte/omi-forecast

# using git (SSH recommended)
git clone git@github.com:baggiponte/omi-forecast
```

> **Note**
>
> 🎬 How to configure SSH
>
> Cloning over SSH is safer. Follow [this guide](https://www.youtube.com/watch?v=5o9ltH6YmtM).
> Alternatively, you can follow the steps in [this](https://github.com/git-merge-workshops/simplify-signing-with-ssh/blob/main/exercises/01-setup-workstation.md) workshop of GitHub's.

2. Install `pdm`:

```bash
pipx install pdm
```

> **Warning**
>
> 🔎 Why `pipx`?
> `pip install --user` is not recommended, as it does not ensure dependency isolation. For this purpose, the [Python Packaging Authority (PyPA)](https://www.pypa.io/en/latest/) advises to use [`pipx`](https://pypa.github.io/pipx/). `pipx` installs and runs python CLIs in isolated environments. To install it, follow the instructions [here](https://pypa.github.io/pipx/#install-pipx).

3. Install production and development dependencies.

```
just install
```

### Before submitting a PR

Run the following:

```
just pre-release
just test
```

The following operations will be performed:

1. Format with `black` and `isort`.
2. Lint with `ruff`.
3. Run type checks with `mypy`.
4. Audit dependencies with `pip-audit`.
5. Check commit messages are consistent with Conventional Commits using `commitizen`.
6. Check whether a version bump is possible.
7. Run all tests.
