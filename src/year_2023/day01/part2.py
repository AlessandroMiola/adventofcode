import os
import re

from src.year_2023.utils import read_file


def extract_calibration_value(input_str: str) -> int:
    str2digit = {
        word: str(idx + 1)
        for idx, word in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        )
    }

    def build_subpattern(str2digit: dict[str, str]) -> str:
        subpattern = ""
        for k, _ in str2digit.items():
            subpattern += k + "|"
        return subpattern

    try:
        subpattern = build_subpattern(str2digit) + r"\d"
        matches = []
        while match := re.search(subpattern, input_str):
            matches.append(input_str[match.start() : match.end()])
            if len(match.group()) > 1:
                input_str = input_str[match.end() - 1 :]
            else:
                input_str = input_str[match.end() :]
        decoded_matches = [str2digit[match] if match in str2digit else match for match in matches]
        return int(decoded_matches[0] + decoded_matches[-1])
    except IndexError:
        return 0


def sum_calibration_values(file_path: str) -> int:
    def _read_file(file_path: str) -> list[str]:
        return read_file(file_path)

    lines = _read_file(file_path)
    return sum(extract_calibration_value(line) for line in lines)


if __name__ == "__main__":
    file_name = "input_file.txt"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "data", file_name)
    print(f"Sum of calibration values is: {sum_calibration_values(file_path)}")
