import os

from functools import reduce
from operator import mul

from src.year_2023.day02.part1 import get_ncubes_combination_per_game
from src.year_2023.utils import read_file


def get_min_ncubes_to_play(input_str: str) -> list[int]:
    return [
        max(cube) for cube in zip(*get_ncubes_combination_per_game(input_str))
    ]


def sum_power_ncubes(file_path: str) -> int:
    def _read_file(file_path: str) -> list[str]:
        return read_file(file_path)
    lines = _read_file(file_path)
    return sum(
        reduce(mul, get_min_ncubes_to_play(line)) for line in lines
    )


if __name__ == "__main__":
    file_name = "input_file.txt"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "data", file_name)
    print(f"Sum of power is: {sum_power_ncubes(file_path)}")
