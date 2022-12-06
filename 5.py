from copy import deepcopy
from typing import Tuple
from aoc22.parse import load


def clean_crate(crate: str) -> str:
    return crate.replace("[", "").replace("]", "")

def parse_instruction(instruction: str) -> Tuple[int, int, int]:
    spl = instruction.split()
    return (int(spl[1]), int(spl[3]), int(spl[-1]))

if __name__ == "__main__":
    lines = load("inputs/5.txt")
    idx = 0
    while lines[idx] != '':
        idx += 1
    stack_lines = list(map(lambda sl: sl.split(' '), lines[:idx]))
    instructions = lines[idx + 1:]
    # print(stack_lines)
    # print(instructions)    
    stacks = [[] for _ in range(len(stack_lines))]
    for stack_line in stack_lines[:-1][::-1]:
        cur_stack = 0
        i = 0
        while i < len(stack_line):
            if stack_line[i] == '':
                i += 4
                cur_stack += 1
                continue
            stacks[cur_stack].append(clean_crate(stack_line[i]))
            cur_stack += 1
            i += 1
    stacks_res1 = deepcopy(stacks)
    for instruction in instructions:
        (n, inp, out) = parse_instruction(instruction)
        for _ in range(n):
            stacks_res1[out - 1].append(stacks_res1[inp -1].pop())
    res1 = ''.join(s[-1] for s in stacks_res1)
    print(res1)

    stacks_res2 = deepcopy(stacks)
    for instruction in instructions:
        (n, inp, out) = parse_instruction(instruction)
        if n > 1:
            stacks_res2[out - 1] += stacks_res2[inp - 1][-n:]
            stacks_res2[inp - 1] = stacks_res2[inp - 1][:-n]
        else:
            stacks_res2[out - 1].append(stacks_res2[inp -1].pop())
            n -= 1
        # while n > 0:
            # if n >= 3:
            #     stacks_res2[out - 1] += stacks_res2[inp - 1][-3:]
            #     stacks_res2[inp - 1] = stacks_res2[inp - 1][:-3]
            #     n -= 3
            # elif n >= 2:
            #     stacks_res2[out - 1] += stacks_res2[inp -1][-2:]
            #     stacks_res2[inp - 1] = stacks_res2[inp - 1][:-2]
            #     n -= 2
            # else:
            #     stacks_res2[out - 1].append(stacks_res2[inp -1].pop())
            #     n -= 1
        # import pdb; pdb.set_trace()
    res2 = ''.join(s[-1] for s in stacks_res2)
    print(res2)

    # res2 = ''.join(s[-1] for s in stacks_res2)
    # print(res2)