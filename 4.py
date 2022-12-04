from collections import Counter
from functools import reduce
from typing import Tuple
from aoc22.parse import load

Range = Tuple[int, int]

def one_range_contains_other(r1: Range, r2: Range) -> bool:
    if r1[0] == r2[0]:
        return r1[-1] <= r2[-1] or r2[-1] <= r1[-1]
    if r1[0] < r2[0]:
        return r2[-1] <= r1[-1]
    return one_range_contains_other(r2, r1)

def ranges_overlap(r1: Range, r2: Range) -> bool: 
    return len(set(range(r1[0], r1[-1] + 1)).intersection(range(r2[0], r2[-1] + 1))) > 0


if __name__ == "__main__":
    lines = load("inputs/4.txt")
    pairs = [(tuple(map(int, line.split(",")[0].split("-"))), tuple(map(int, line.split(",")[1].split("-")))) for line in lines]
    res1 = sum([one_range_contains_other(r1, r2) for r1, r2 in pairs])
    print(res1)
    res2 = sum([ranges_overlap(r1, r2) for r1, r2 in pairs])
    print(res2)
    # for (r1, r2) in pairs:
    #     print(r1, r2, ranges_overlap(r1, r2))
