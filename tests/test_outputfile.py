import os
import pytest
from main import process_file

@pytest.fixture
def input_file_path(tmp_path):
    # Create a temporary input file for testing
    input_text = "This is a sample text with dates like 2023-05-21, phone numbers like 123-456-7890, addresses like 123 Main St, and names like John Doe."
    input_file = tmp_path / "sample_text.txt"
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(input_text)
    return input_file

def test_output_file_creation(input_file_path, tmp_path):
    # Arguments for redaction
    args = type('', (), {})()  # Creating a simple namespace object
    args.input = input_file_path
    args.output = tmp_path
    args.date = True
    args.phone = True
    args.address = True
    args.name = True
    
    # Execute the processing function
    process_file(input_file_path, args)
    
    # Check if output file is created
    output_file_path = os.path.join(tmp_path, os.path.basename(input_file_path) + '.censored')
    assert os.path.exists(output_file_path), "Output file is not created."
    
    # Clean up: remove output file
    os.remove(output_file_path)


