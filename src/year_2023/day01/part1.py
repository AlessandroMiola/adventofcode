import os
import re

from src.year_2023.utils import read_file


def extract_calibration_value(input_str: str) -> int:
    try:
        return int(
            re.findall(r"\d", input_str)[0] + re.findall(r"\d", input_str)[-1]
        )
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
