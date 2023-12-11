import os

import pytest

from src.year_2023.day02.part2 import (
    get_min_ncubes_to_play,
    sum_power_ncubes
)


@pytest.fixture
def mock_file_data(tmp_path):
    test_file_path = os.path.join(tmp_path, "test_file.txt")
    test_input = (
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n"
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n"
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n"
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n"
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    )
    with open(test_file_path, "w") as file:
        file.write(test_input)
    return test_file_path


@pytest.mark.parametrize(
    ["test_inputs", "test_results"],
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", [4, 2, 6]),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", [1, 3, 4]),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", [20, 13, 6]),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", [14, 3, 15]),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", [6, 3, 2]),
        ("Game 6: ", [0, 0, 0]),
    ]
)
def test_get_min_ncubes_to_play(test_inputs, test_results):
    assert get_min_ncubes_to_play(test_inputs) == test_results


def test_sum_power_ncubes(mock_file_data):
    assert sum_power_ncubes(mock_file_data) == 2286
