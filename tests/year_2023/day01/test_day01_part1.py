import os

import pytest

from src.year_2023.day01.part1 import (
    extract_calibration_value,
    sum_calibration_values
)


@pytest.fixture
def mock_file_data(tmp_path):
    test_file_path = os.path.join(tmp_path, "test_file.txt")
    test_input = (
        "1abc2\n"
        "pqr3stu8vwx\n"
        "a1b2c3d4e5f\n"
        "treb7uchet"
    )
    with open(test_file_path, "w") as file:
        file.write(test_input)
    return test_file_path


@pytest.mark.parametrize(
    ["test_inputs", "test_results"],
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("yewiu0fegrwh", 0),
        ("", 0),
        ("jhdjdkaddas", 0)
    ]
)
def test_extract_calibration_value(test_inputs, test_results):
    assert extract_calibration_value(test_inputs) == test_results


def test_sum_calibration_values(mock_file_data):
    assert sum_calibration_values(mock_file_data) == 142
