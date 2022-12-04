from collections import Counter
from functools import reduce
from aoc22.parse import load

def priority(c: str):
    if ord(c) > ord('a') :
        return ord(c) - 96
    return ord(c) - 64 + 26


if __name__ == "__main__":
    lines = load("inputs/3.txt")
    rucksacks = [(Counter(l[:len(l)//2]), Counter(l[len(l)//2:])) for l in lines]
    item_types = [set(c1.keys()).intersection(set(c2.keys())).pop() for (c1, c2) in rucksacks]
    res1= sum([priority(it) for it in item_types])
    print(res1)
    item_types_counter = Counter(item_types)
    print(item_types_counter)
    print(len(lines))   
    res2= sum([priority(set(lines[i*3]).intersection(set(lines[i*3+1]).intersection(set(lines[i*3+2]))).pop()) for i in range(len(lines) // 3)])
    print(res2)