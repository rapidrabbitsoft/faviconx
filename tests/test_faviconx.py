import os
import shutil
import tempfile
from pathlib import Path
from click.testing import CliRunner
from PIL import Image
import pytest

from faviconx.__main__ import main, ICON_SIZES

def create_sample_image(path, size=(256, 256), color=(255, 0, 0, 255)):
    """Create a simple PNG image for testing."""
    img = Image.new('RGBA', size, color)
    img.save(path)

@pytest.fixture(scope="module")
def sample_image(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("data")
    img_path = tmp_dir / "sample.svg"
    create_sample_image(img_path)
    return img_path

@pytest.fixture
def temp_output_dir(tmp_path):
    return tmp_path / "output"

def test_cli_required(sample_image, temp_output_dir):
    runner = CliRunner()
    result = runner.invoke(main, [str(sample_image), str(temp_output_dir), '--filter', 'required'])
    assert result.exit_code == 0
    # Check that required icons are generated
    for icon in ICON_SIZES:
        if icon['status'] == 'R':
            filename = icon['filename'].replace('favicon', 'icon', 1)
            assert (temp_output_dir / filename).exists()

def test_cli_prefix(sample_image, temp_output_dir):
    runner = CliRunner()
    prefix = 'testico'
    result = runner.invoke(main, [str(sample_image), str(temp_output_dir), '--prefix', prefix, '--filter', 'required-recommended'])
    assert result.exit_code == 0
    # Check that files use the prefix
    for icon in ICON_SIZES:
        if icon['status'] in {'R', 'RC'}:
            filename = icon['filename'].replace('favicon', prefix, 1)
            assert (temp_output_dir / filename).exists()

def test_cli_optional(sample_image, temp_output_dir):
    runner = CliRunner()
    result = runner.invoke(main, [str(sample_image), str(temp_output_dir), '--filter', 'optional'])
    assert result.exit_code == 0
    # Check that optional icons are generated
    for icon in ICON_SIZES:
        if icon['status'] in {'R', 'RC', 'O'}:
            filename = icon['filename'].replace('favicon', 'icon', 1)
            assert (temp_output_dir / filename).exists()

def test_cli_all(sample_image, temp_output_dir):
    runner = CliRunner()
    result = runner.invoke(main, [str(sample_image), str(temp_output_dir), '--filter', 'all'])
    assert result.exit_code == 0
    # Check that all icons are generated
    for icon in ICON_SIZES:
        filename = icon['filename'].replace('favicon', 'icon', 1)
        assert (temp_output_dir / filename).exists()

def test_cli_error_on_missing_image(temp_output_dir):
    runner = CliRunner()
    result = runner.invoke(main, ["notfound.png", str(temp_output_dir)])
    assert result.exit_code != 0
    assert "Source image not found" in result.output 