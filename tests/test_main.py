import pytest
import os
import shutil
from main import redact_text, process_file
import argparse

@pytest.fixture(scope="module")
def test_files(tmpdir_factory):
    input_dir = tmpdir_factory.mktemp("input")
    output_dir = tmpdir_factory.mktemp("output")

    # Create input files
    file1 = input_dir.join("file1.txt")
    file1.write("Some text with a date: 2023-01-01 and a phone number: 123-456-7890.")

    file2 = input_dir.join("file2.txt")
    file2.write("Another text with an address: 123 Main St and a name: John Doe.")

    yield str(input_dir), str(output_dir)

    # Clean up
    shutil.rmtree(str(input_dir))
    shutil.rmtree(str(output_dir))

def test_redact_text(test_files):
    input_dir, output_dir = test_files

    input_file = os.path.join(input_dir, "file1.txt")
    output_file = os.path.join(output_dir, "file1.txt.censored")

    redacted_text = redact_text("Some text with a date: 2023-01-01 and a phone number: 123-456-7890.", None, argparse.Namespace(date=True, phone=True, address=False, name=False))

    assert "2023-01-01" not in redacted_text
    assert "123-456-7890" not in redacted_text

def test_process_file(test_files):
    input_dir, output_dir = test_files

    input_file = os.path.join(input_dir, "file1.txt")
    output_file = os.path.join(output_dir, "file1.txt.censored")

    process_file(input_file, argparse.Namespace(date=True, phone=True, address=False, name=False))

    assert os.path.exists(output_file)
    with open(output_file, "r", encoding="utf-8") as f:
        redacted_text = f.read()

    assert "2023-01-01" not in redacted_text
    assert "123-456-7890" not in redacted_text
