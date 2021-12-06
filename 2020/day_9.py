#!python3

from typing import List, Union, Tuple
import os
from itertools import combinations

ROOT = "C:\\Users\\RuweBo01\\Anaconda3\\Scripts\\Advent of code"
input_filee = "9_input.txt"
input_file = os.path.join(ROOT, input_filee)


def parse_input(txt_file: str = input_file) -> List[str]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


input_list = [int(x) for x in parse_input()]


def find_pairs(lst: List[int], K: int, N: int) -> Union[tuple, int]:
    res = [pair for pair in combinations(lst, N) if sum(pair) == K]
    if res:
        return res
    else:
        print(f"Failed to find combination for inputs {K}, {N}")
        return K


def assignment_1(inp: List[int], p: int) -> int:
    for idx in range(p, len(inp)):
        l = inp[(idx-p):idx]
        result = find_pairs(l, inp[idx], 2)
        if isinstance(result, list):
            continue
        else:
            break
    return result

def find_number_range(inp: List[int], p: int) -> Tuple[int, int]:
    max = assignment_1(inp, p)
    max_idx = inp.index(max)
    l = inp[:max_idx]
    
    for i in range(len(l)):
        res = l[i]
        j = i + 1
        while j < len(l):
            # print(f"{res} + {l[j]} = {res+l[j]}")
            res += l[j]
            if res > max:
                break
            elif res == max:
                return(l[i], l[j])
            j += 1

def assignment_2(inp: List[int], p: int):
    first, last = find_number_range(inp, p)
    first_pos = inp.index(first)
    last_pos = inp.index(last)
    lowest = min(inp[first_pos:last_pos])
    highest = max(inp[first_pos:last_pos])
    return(lowest+highest)

print(assignment_2(input_list, 25))




