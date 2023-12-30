import os

import pytest

from src.year_2023.day04.part1 import get_points_per_game, sum_points


@pytest.fixture
def mock_file_data(tmp_path):
    test_file_path = os.path.join(tmp_path, "test_file.txt")
    test_input = (
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n"
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n"
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n"
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n"
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n"
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    )
    with open(test_file_path, "w") as file:
        file.write(test_input)
    return test_file_path


@pytest.mark.parametrize(
    ["test_inputs", "test_results"],
    [
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 8),
        ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2),
        ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 2),
        ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1),
        ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0),
        ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0),
    ],
)
def test_get_points_per_game(test_inputs, test_results):
    assert get_points_per_game(test_inputs) == test_results


def test_sum_points(mock_file_data):
    assert sum_points(mock_file_data) == 13
