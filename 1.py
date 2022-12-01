from aoc22.parse import load
from dataclasses import dataclass
from functools import reduce

@dataclass
class Elf:
    calories: int = 0
    def add_calories(self, calories) -> None:
        self.calories += calories

    def __lt__(self, elf):
        return ((self.calories) < (elf.calories))

    def __gt__(self, elf):
        return ((self.calories) > (elf.calories))

    def __le__(self, elf):
        return ((self.calories) <= (elf.calories))

    def __ge__(self, elf):
        return ((self.calories) >= (elf.calories))

    def __eq__(self, elf):
        return ((self.calories) == (elf.calories))


if __name__ == "__main__":
    lines = load("inputs/1.txt")
    elves = []
    cur_elf = Elf()
    for line in lines:
        if line != '':
            cur_elf.add_calories(int(line))
        else:
            elves.append(cur_elf)
            cur_elf = Elf()
    sorted_elves = sorted(elves)

    print(sorted_elves[-1].calories)
    print(reduce(lambda s, elf: s + elf.calories, sorted_elves[-3:], 0))