import abc
from aoc22.parse import load
from dataclasses import dataclass
from functools import reduce, total_ordering
from enum import Enum

@total_ordering
class Shape(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3
    @staticmethod
    def to_shape(s: str) -> 'Shape':
        match s:
            case "A" | "X": return Shape.Rock
            case "B" | "Y": return Shape.Paper
            case "C" | "Z": return Shape.Scissors
    def __gt__(self, other):
        match (self, other):
            case (Shape.Rock, Shape.Paper): return False
            case (Shape.Paper, Shape.Rock): return True
            case (Shape.Rock, Shape.Scissors): return True
            case (Shape.Scissors, Shape.Rock): return False
            case (Shape.Scissors, Shape.Paper): return True
            case (Shape.Paper, Shape.Scissors): return False
            case _: return False

@dataclass
class Round:
    input_shape: Shape
    output_shape: Shape
    @property
    def score(self):
        return self.output_shape.value + self.outcome
        
    @property
    def outcome(self):
        if self.output_shape > self.input_shape: 
            return 6
        elif self.output_shape == self.input_shape:
            return 3
        return 0

if __name__ == "__main__":
    lines = load("inputs/2.txt")
    rounds = [Round(Shape.to_shape(line.split()[0]), Shape.to_shape(line.split()[-1])) for line in lines]
    for round in rounds:
        print(round)
    print(reduce(lambda s, r: r.score + s, rounds, 0))
    round2_score = 0
    for line in lines:
        input_, output_ = line.split()
        if output_ == "X":
            match input_:
                case "A": round2_score += 3
                case "B": round2_score += 1
                case "C": round2_score += 2
        elif output_ == "Y":
            round2_score += Shape.to_shape(input_).value + 3
        else:
            match input_:
                case "A": round2_score += 2
                case "B": round2_score += 3
                case "C": round2_score += 1
            round2_score += 6
    print(round2_score)
    # print(Round("A", "X").score)
    # print(Round("A", "Y").score)
    # print(Round("A", "Z").score)
    # print(Round("B", "X").score)
    # print(Round("B", "Y").score)
    # print(Round("B", "Z").score)
    # print(Round("C", "X").score)
    # print(Round("C", "Y").score)
    # print(Round("C", "Z").score)