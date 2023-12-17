import os
import re

from src.year_2023.utils import read_file
from src.year_2023.day06.part1 import (
    get_n_winning_combinations as _get_n_winning_combinations
)


def get_time_and_winning_distance(lines: list[str]) -> tuple[int]:
    time = int(''.join(num for num in re.findall(r"\b\d+", lines[0])))
    distance = int(''.join(num for num in re.findall(r"\b\d+", lines[1])))
    return time, distance


def get_n_winning_combinations(file_path: str) -> int:
    lines = read_file(file_path)
    time, distance = get_time_and_winning_distance(lines)
    return _get_n_winning_combinations(time, distance)


if __name__ == "__main__":
    file_name = "input_file.txt"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "data", file_name)
    print(
        f"The total number of winning combinations is: "
        f"{get_n_winning_combinations(file_path)}"
    )
