import pytest
import spacy
from censoror import redact_text, process_file

# Load spaCy model once and use it across tests for efficiency.
@pytest.fixture(scope="module")
def nlp():
    return spacy.load("en_core_web_md")

@pytest.fixture
def args():
    class Args:
        def __init__(self, dates=False, phones=False, address=False, names=False, input=None, output=None):
            self.dates = dates
            self.phones = phones
            self.address = address
            self.names = names
            self.input = input
            self.output = output
    return Args

@pytest.fixture
def setup_file_system(tmp_path):
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    input_file = input_dir / "test_file.txt"
    input_file.write_text("She moved to America after she got a job.")
    return input_file, output_dir

# Test redacting dates.
def test_redact_dates(nlp, args):
    args = args(dates=True)
    text = "She was born on January 1, 2000."
    expected = "She was born on ███████████████."
    assert redact_text(text, nlp, args) == expected


# def test_redact_addresses(nlp, args):
#     args = args(address=True)
#     # Example text containing entities that should be recognized as GPE, FAC, LOC
#     text = "She moved to america after she got a job"

#     # Expected output after redaction
#     expected_redacted_text = "She moved to ███████ after she got a job"

#     # Assert the redacted text is as expected
#     assert redact_text(text, nlp, args) == expected_redacted_text


# Test not redacting when flags are not set.
def test_no_redaction(nlp, args):
    args = args()  # All flags set to False.
    text = "She was born on January 1, 2000, and her phone number is 123-456-7890."
    # Expecting no redaction since no flags are true.
    assert redact_text(text, nlp, args) == text


def test_process_file(nlp, args, setup_file_system):
    input_file, output_dir = setup_file_system
    arg_vals = args(address=True, input=str(input_file), output=str(output_dir))
    process_file(str(input_file), arg_vals)

    output_file = output_dir / "test_file.censored"
    assert output_file.exists()

    # expected_output = "She moved to ███████ after she got a job."
    # with open(output_file, 'r', encoding='utf-8') as f:
    #     content = f.read()

    # assert content == expected_output


def test_process_file_no_redaction(nlp, args, setup_file_system):
    input_file, output_dir = setup_file_system
    # Not setting any flag to true, so no redaction should occur.
    arg_vals = args(input=str(input_file), output=str(output_dir))
    process_file(str(input_file), arg_vals)

    output_file = output_dir / "test_file.censored"
    assert output_file.exists()

    # The output should be the same as the input in this case.
    expected_output = "She moved to America after she got a job."
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    assert content == expected_output

