import os
import re

from src.year_2023.utils import read_file


def get_len_input(input_lines: list[str]) -> int:
    return len(input_lines[0])


def get_numbers_pos(input_lines: list[str]) -> list[tuple[int]]:
    len_input = get_len_input(input_lines)
    return [
        (idx * len_input + match.start(), idx * len_input + match.end(), int(match.group()))
        for idx, line in enumerate(input_lines)
        for match in re.finditer(r"\d+", line)
    ]


def get_symbols_pos(input_lines: list[str]) -> list[int]:
    len_input = get_len_input(input_lines)
    return [
        (idx * len_input + match.start())
        for idx, line in enumerate(input_lines)
        for match in re.finditer(r"[^.\d]", line)
    ]


def get_candidate_pnum_symbols_pos(
    number_pos: tuple[int],
    len_input: int
) -> list[int]:
    num_p_start, num_p_end, _ = number_pos
    return sorted(
        list(
            set(
                range(num_p_start - len_input - 1, num_p_end - len_input + 1)
            ).union(
                set(range(num_p_start - 1, num_p_start))
            ).union(
                set(range(num_p_end, num_p_end + 1))
            ).union(
                set(range(num_p_start + len_input - 1, num_p_end + len_input + 1))
            )
        )
    )


def sum_part_numbers(file_path: str) -> int:
    input_lines = read_file(file_path)
    len_input = get_len_input(input_lines)
    numbers_pos = get_numbers_pos(input_lines)
    symbols_pos = get_symbols_pos(input_lines)
    sum = 0
    for num_p_start, num_p_end, num in numbers_pos:
        candidate_symbols_pos = get_candidate_pnum_symbols_pos(
            (num_p_start, num_p_end, num),
            len_input
        )
        for sym_p_start in symbols_pos:
            if sym_p_start in candidate_symbols_pos:
                sum += num
                break
    return sum


if __name__ == "__main__":
    file_name = "input_file.txt"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "data", file_name)
    print(f"Sum of part numbers is: {sum_part_numbers(file_path)}")
