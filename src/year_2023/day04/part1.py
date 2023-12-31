import os
import re

from src.year_2023.utils import read_file


def get_n_matches_per_game(line: str) -> int:
    available_set_numbers = set(re.findall(r"\d+", line.split(": ")[1].split(" | ")[0]))
    winning_set_numbers = set(re.findall(r"\d+", line.split(" | ")[1]))
    return len(available_set_numbers.intersection(winning_set_numbers))


def get_points_per_game(line: str) -> int:
    n_matches = get_n_matches_per_game(line)
    return 2 ** (n_matches - 1) if n_matches > 0 else 0


def sum_points(file_path: str) -> int:
    lines = read_file(file_path)
    return sum(get_points_per_game(line) for line in lines)


if __name__ == "__main__":
    file_name = "input_file.txt"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "data", file_name)
    print(f"Sum of winning numbers is: {sum_points(file_path)}")
