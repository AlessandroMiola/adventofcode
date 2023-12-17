import os

import pytest

from src.year_2023.day06.part2 import get_n_winning_combinations


@pytest.fixture
def mock_file_data(tmp_path):
    test_file_path = os.path.join(tmp_path, "test_file.txt")
    test_input = (
        "Time:      7  15   30\n"
        "Distance:  9  40  200"
    )
    with open(test_file_path, "w") as file:
        file.write(test_input)
    return test_file_path


def test_get_n_winning_combinations(mock_file_data):
    assert get_n_winning_combinations(mock_file_data) == 71503
