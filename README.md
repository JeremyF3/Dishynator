# Dishynator

Application to analyze plant images.

# Development

Using [uv](https://docs.astral.sh/uv/) to manage python packages.

## Setup

```bash
uv pip install .
```

# Install production + dev + test dependencies

```bash
uv pip install ".[dev,test]"
```

# Install all optional dependencies

```bash
uv pip install ".[dev,test,docs]"
```

## To generate requirements.txt

```bash
uv pip compile pyproject.toml -o requirements.txt
```

