def read_file(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return list(file.read().split("\n"))
