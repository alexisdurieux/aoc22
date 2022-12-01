from typing import List


def load(filename: str) -> List[str]:
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]
