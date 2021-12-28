from __future__ import annotations
from os import replace
from pathlib import Path
from time import perf_counter
from itertools import permutations
import math
import re


input_file = Path(__file__).parent / "inputs" / "d18.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()


def depth(s: str | list) -> int | int:
    depth = 0
    max_depth = 0
    max_depth_start_location = None
    for i, letter in enumerate(s):
        if letter == '[':
            depth += 1
            if depth > max_depth:
                max_depth = depth
            if depth > 4 and not max_depth_start_location:
                max_depth_start_location = i
        elif letter == ']':
            depth -= 1
    return max_depth, max_depth_start_location


def listify(s: str) -> list[str]:
    l = []
    continue_next = False
    for i, c in enumerate(s[1:]):
        if continue_next:
            continue_next = False
            continue
        if s[i] in ['[', ']', ','] or c in ['[', ']', ',']:
            l.append(s[i])
        else:
            l.append(s[i]+c)
            continue_next = True
    l.append(c)
    return l


def split(s: str) -> str:
    s_list = '[' + s.replace('[', '').replace(']', '') + ']'
    list_of_numbers = eval(s_list)
    for num in list_of_numbers:
        if num > 9:
            rounded = num / 2
            new_num = [math.floor(rounded), math.ceil(rounded)]
            idx = s.index(str(num))
            s = s[:idx] + str(new_num).replace(' ', '') + s[idx+2:]
            # print(f'Split {num}:\t\t{s}')
            return s, True
    return s, False


def explode(s: str) -> str | bool:
    l = listify(s)
    loc = depth(l)[1]
    if not loc:
        return s, False
    loc_1 = loc_2 = loc
    left_num = int(l[loc + 1])
    right_num = int(l[loc + 3])

    # Get first number to the left
    i = 1
    while i < loc:
        c = l[loc-i]
        if c not in ['[', ']', ',']:
            res = int(c) + left_num
            l[loc-i] = str(res)
            break
        i += 1
    # Change first number to the right
    j = 4
    while loc + j < len(l):
        c = l[loc+j]
        if c not in ['[', ']', ',']:
            res = int(c) + right_num
            l[loc+j] = str(res)
            break
        j += 1
    l1 = ''.join(l[:loc_1])
    l2 = ''.join(l[loc_2+5:])

    # Replace deepest nest with 0
    s = l1 + '0' + l2
    # print(f'Exploded {left_num, right_num}:\t{s}')
    return s, True


def reduce(s: str) -> str:
    while True:
        s, exploded = explode(s)
        if exploded:
            continue
        s, was_split = split(s)
        if not was_split and not exploded:
            return s


def replace_in_string(s: str, original: str, replacement: str) -> str:
    l = [x for x in s]
    start = s.find(original)
    end = start + len(original)
    l1 = ''.join(l[:start])
    l2 = ''.join(l[end:])
    return l1 + replacement + l2


def calculate_magnitude(s: str) -> int:
    pattern = r'\[\d+,\d+\]'
    while True:
        pairs = re.findall(pattern, s)
        for pair_string in pairs:
            pair = eval(pair_string)
            magnitude = (3*pair[0]) + (2*pair[1])
            s = replace_in_string(s, pair_string, str(magnitude))
        if '[' in s:
            continue
        return int(s)


def solve(data: list[str], result: int = 0, part1=True) -> int:
    if part1:
        num = data[0]
        for row in data[1:]:
            num_to_analyze = f'[{num},{row}]'
            # print(f'Start:\t\t\t{num_to_analyze}')
            num = reduce(num_to_analyze)
        result = calculate_magnitude(num)
        return result
    max_magnitude = 0
    for perm in permutations(data, 2):
        num = reduce(f'[{perm[0]},{perm[1]}]')
        magnitude = calculate_magnitude(num)
        if magnitude > max_magnitude:
            max_magnitude = magnitude
    return max_magnitude
    

timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
