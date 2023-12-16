import os

from src.year_2023.day04.part1 import get_n_matches_per_game
from src.year_2023.utils import read_file


def get_n_scratchcards_per_game(lines: list[str]) -> dict[int, int]:
    n_matches = [get_n_matches_per_game(line) for line in lines]
    n_scratchcards = {idx + 1: 1 for idx, _ in enumerate(n_matches)}
    for game, matches in enumerate(n_matches):
        for idx in range(1, matches + 1):
            n_scratchcards[game + 1 + idx] += n_scratchcards.get(game + 1)
    return n_scratchcards


def sum_scratchcards(file_path: str) -> int:
    lines = read_file(file_path)
    return sum(v for _, v in get_n_scratchcards_per_game(lines).items())


if __name__ == "__main__":
    file_name = "input_file.txt"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "data", file_name)
    print(f"Sum of winning numbers is: {sum_scratchcards(file_path)}")
