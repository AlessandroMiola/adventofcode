import os
import re
import typing

from functools import reduce

from src.year_2023.utils import read_file


def get_time_and_winning_distance_per_race(lines: list[str]) -> typing.Iterator:
    times = [int(num) for num in re.findall(r"\b\d+", lines[0])]
    distances = [int(num) for num in re.findall(r"\b\d+", lines[1])]
    return zip(times, distances)


def get_n_winning_combinations(time: int, distance: int) -> int:
    return sum((time - hb) * hb > distance for hb in range(1, time + 1))


def get_product_winning_combinations(file_path: str) -> int:
    lines = read_file(file_path)
    products_gen = (
        get_n_winning_combinations(time, distance)
        for time, distance in get_time_and_winning_distance_per_race(lines)
    )
    return reduce(lambda x, y: x * y, products_gen, 1)


if __name__ == "__main__":
    file_name = "input_file.txt"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "data", file_name)
    print(
        f"The product of winning combinations is: "
        f"{get_product_winning_combinations(file_path)}"
    )
