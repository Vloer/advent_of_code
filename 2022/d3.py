from __future__ import annotations
from pathlib import Path
from time import perf_counter
from string import ascii_lowercase, ascii_uppercase

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw',
]
priority = ascii_lowercase + ascii_uppercase


def solve(data: list[str], result: int = 0, part1=True) -> int:
    if part1:
        sum = 0
        for bag in data:
            a, b = bag[:len(bag)//2], bag[len(bag)//2:]
            for letter in a:
                if letter in b:
                    prio = priority.index(letter) + 1
                    sum += prio
                    break
        return sum
    else:
        sum = 0
        for i in range(0, len(data), 3):
            a, b, c = data[i], data[i+1], data[i+2]
            for letter in a:
                if letter in b:
                    if letter in c:
                        prio = priority.index(letter) + 1
                        sum += prio
                        break
        return sum


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
