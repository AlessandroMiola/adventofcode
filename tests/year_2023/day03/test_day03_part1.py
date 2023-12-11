import os

import pytest

from src.year_2023.day03.part1 import sum_part_numbers


@pytest.fixture
def mock_file_data(tmp_path):
    test_file_path = os.path.join(tmp_path, "test_file.txt")
    test_input = (
        "467..114..\n"
        "...*......\n"
        "..35..633.\n"
        "......#...\n"
        "617*......\n"
        ".....+.58.\n"
        "..592.....\n"
        "......755.\n"
        "...$.*....\n"
        ".664.598.."
    )
    with open(test_file_path, "w") as file:
        file.write(test_input)
    return test_file_path


def test_sum_part_numbers(mock_file_data):
    assert sum_part_numbers(mock_file_data) == 4361
