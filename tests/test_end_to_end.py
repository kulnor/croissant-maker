"""End-to-end tests for Croissant Maker using real datasets."""

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from croissant_maker.__main__ import app

runner = CliRunner()


@pytest.fixture
def mimiciv_demo_path() -> Path:
    """Path to the MIMIC-IV demo dataset for testing."""
    dataset_path = (
        Path(__file__).parent
        / "data"
        / "input"
        / "mimiciv_demo"
        / "physionet.org"
        / "files"
        / "mimic-iv-demo"
        / "2.2"
    )

    if not dataset_path.exists():
        pytest.skip(f"MIMIC-IV demo dataset not found at {dataset_path}")

    return dataset_path


@pytest.fixture
def output_dir() -> Path:
    """Create and return the tests/output directory."""
    output_path = Path(__file__).parent / "data" / "output"
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def test_mimiciv_demo_generation(mimiciv_demo_path: Path, output_dir: Path) -> None:
    """Test end-to-end metadata generation with MIMIC-IV demo dataset."""
    output_file = output_dir / "mimiciv_demo_croissant.jsonld"

    result = runner.invoke(
        app,
        [
            "-i",
            str(mimiciv_demo_path),
            "-o",
            str(output_file),
            "--name",
            "MIMIC-IV Demo Dataset",
            "--description",
            "Demo subset of MIMIC-IV, a freely accessible electronic health record dataset from Beth Israel Deaconess Medical Center (2008-2019)",
            "--url",
            "https://physionet.org/content/mimic-iv-demo/",
            "--license",
            "PhysioNet Restricted Health Data License 1.5.0",
            "--dataset-version",
            "2.2",
            "--date-published",
            "2023-01-06",
            "--creator",
            "Alistair Johnson,aewj@mit.edu,https://physionet.org/",
            "--creator",
            "Lucas Bulgarelli,,https://mit.edu/",
            "--creator",
            "Tom Pollard,tpollard@mit.edu,https://physionet.org/",
            "--creator",
            "Steven Horng,,https://www.bidmc.org/",
            "--creator",
            "Leo Anthony Celi,lceli@mit.edu,https://lcp.mit.edu/",
            "--creator",
            "Roger Mark,,https://lcp.mit.edu/",
            "--citation",
            "Johnson, A., Bulgarelli, L., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2023). MIMIC-IV (version 2.2). PhysioNet. https://doi.org/10.13026/6mm1-ek67",
        ],
    )

    assert result.exit_code == 0, f"Command failed: {result.stdout}"
    assert output_file.exists(), "Output file was not created"

    # Validate the generated metadata
    with open(output_file) as f:
        metadata = json.load(f)

    assert metadata["name"] == "MIMIC-IV Demo Dataset"
    assert metadata["version"] == "2.2"
    assert metadata["url"] == "https://physionet.org/content/mimic-iv-demo/"
    assert len(metadata["creator"]) == 6  # Six creators
    assert len(metadata["distribution"]) > 20  # Many CSV files
    assert len(metadata["recordSet"]) > 10  # Many record sets
