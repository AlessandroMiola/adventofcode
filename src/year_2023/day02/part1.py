import os
import re

from src.year_2023.utils import read_file


def get_ncubes_by_colour_per_game(input_str: str, colour_str: str) -> list[int]:
    return [
        int(el.group()) if el is not None else 0
        for input_substr in input_str.split(";")
        for el in [re.search(rf"\d+(?= {colour_str})", input_substr)]
    ]


def get_ncubes_combination_per_game(input_str: str) -> list[tuple[int]]:
    return list(
        zip(
            get_ncubes_by_colour_per_game(input_str, "red"),
            get_ncubes_by_colour_per_game(input_str, "green"),
            get_ncubes_by_colour_per_game(input_str, "blue"),
        )
    )


def sum_feasible_games_ids(file_path: str) -> int:
    def _read_file(file_path: str) -> list[str]:
        return read_file(file_path)

    lines = _read_file(file_path)
    return sum(
        int(re.search(r"\d+(?=:)", line).group())
        for line in lines
        if all(
            all(el1 <= el2 for el1, el2 in zip(combination, target))
            for combination, target in zip(
                get_ncubes_combination_per_game(line),
                [(12, 13, 14)] * len(get_ncubes_combination_per_game(line)),
            )
        )
    )


if __name__ == "__main__":
    file_name = "input_file.txt"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "data", file_name)
    print(f"Sum of feasible games ids is: {sum_feasible_games_ids(file_path)}")
