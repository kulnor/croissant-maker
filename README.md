# 🥐 Croissant Maker

A tool to automatically generate [Croissant](https://mlcommons.org/en/news/croissant-format-for-ml-datasets/) metadata for datasets, starting with those hosted on [PhysioNet](https://physionet.org/).

*Status: Alpha - Development*

## Installation (Development)

This project uses [uv](https://docs.astral.sh/uv/) for environment and dependency management.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MIT-LCP/croissant-maker.git
    cd croissant-maker
    ```

2.  **Install dependencies:**
    ```bash
    uv sync --group dev
    ```
    This creates a `.venv`, installs the package in editable mode, and includes all development and test dependencies.

3.  **Install the pre-commit hook** (run once; fires automatically on every `git commit` thereafter):
    ```bash
    uv run pre-commit install
    ```

## Usage

After installation, you can use the `croissant-maker` CLI:

```bash
uv run croissant-maker --help
```

### Generate Croissant Metadata

```bash
uv run croissant-maker --input /path/to/dataset --creator "Your Name" --output my-metadata.jsonld
```

### Metadata Override Options

You can override default metadata fields:

```bash
uv run croissant-maker --input /path/to/dataset \
  --name "My Dataset" \
  --description "A machine learning dataset" \
  --creator "John Doe,john@example.com,https://john.com" \
  --creator "Jane Smith,jane@example.com" \
  --license "MIT" \
  --citation "Doe et al. (2024). My Dataset."
```

| Flag | Description | Example | Required |
|------|-------------|---------|----------|
| `--input, -i` | Dataset directory | `--input /data/my-dataset` | Yes |
| `--creator` | Creator info (repeat for multiple) | `--creator "Name,email,url"` | Yes |
| `--output, -o` | Output file | `--output metadata.jsonld` | |
| `--name` | Dataset name | `--name "MIMIC-IV Demo"` | |
| `--description` | Dataset description | `--description "Medical records"` | |
| `--license` | License (SPDX ID or URL) | `--license "MIT"` | |
| `--citation` | Citation text | `--citation "Author (2024)..."` | |
| `--url` | Dataset homepage | `--url "https://example.com"` | |
| `--dataset-version` | Version | `--dataset-version "1.0.0"` | |
| `--date-published` | Publication date | `--date-published "2023-12-15"` | |
| `--no-validate` | Skip validation | `--no-validate` | |
| `--count-csv-rows` | Count exact row numbers for CSV files (slow for large datasets) | `--count-csv-rows` | |

### Validate a Croissant Metadata File

Validation checks that the file can be loaded by `mlcroissant` and conforms to the basic structure of the specification.

```bash
uv run croissant-maker validate my-metadata.jsonld
```

## Testing

```bash
# Run all tests
uv run pytest -v

# Run a single test
uv run pytest tests/test_cli.py::test_creator_formats -v
```

## Pre-Commit Hooks & Code Quality

This project uses `pre-commit` with [Ruff](https://docs.astral.sh/ruff/) to automatically lint and format Python code before commits. Basic configuration file checks (TOML, YAML) are also included.

After running `uv run pre-commit install` once, the hook fires automatically on every `git commit`. To run it manually across all files:

```bash
uv run pre-commit run --all-files
```

## License

MIT License - see [LICENSE](LICENSE) file.
