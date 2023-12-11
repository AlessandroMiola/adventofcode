import os

import pytest

from src.year_2023.day01.part2 import (
    extract_calibration_value,
    sum_calibration_values
)


@pytest.fixture
def mock_file_data(tmp_path):
    test_file_path = os.path.join(tmp_path, "test_file.txt")
    test_input = (
        "two1nine\n"
        "eightwothree\n"
        "abcone2threexyz\n"
        "xtwone3four\n"
        "4nineeightseven2\n"
        "zoneight234\n"
        "7pqrstsixteen"
    )
    with open(test_file_path, "w") as file:
        file.write(test_input)
    return test_file_path


@pytest.mark.parametrize(
    ["test_inputs", "test_results"],
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("", 0),
        ("jhdjdkaddas", 0),
        ("eightwo", 82)
    ]
)
def test_extract_calibration_value(test_inputs, test_results):
    assert extract_calibration_value(test_inputs) == test_results


def test_sum_calibration_values(mock_file_data):
    assert sum_calibration_values(mock_file_data) == 281
