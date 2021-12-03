from __future__ import annotations
from pathlib import Path

input_file = Path(__file__).parent / "inputs" / "d3.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


def get_rate(inp: list(str), reverse=False) -> str:
    max = len(inp)
    rate = ""
    for i in range(len(inp[0])):
        r = 0
        for j in inp:
            r += int(j[i])

        if r >= max/2 and reverse:
            rate += "0"
        elif r < max/2 and not reverse:
            rate += "0"
        else:
            rate += "1"
    return rate


def get_rating(initial: str, inp: list(str), reverse=False) -> str:
    for i in range(len(initial)):
        digit = get_rate(inp, reverse)[i]
        inp = list(filter(lambda num: num[i] == digit, inp))
        if len(inp) == 1:
            return inp[0]


def solve1(inp: list(str) = parse_input()) -> tuple(str, str):
    gamma = get_rate(inp)
    epsilon = get_rate(inp, True)
    result = int(gamma, 2) * int(epsilon, 2)
    print(f"Answer 1: {result}")
    return(gamma, epsilon)


def solve2(gamma: str, epsilon: str, inp: list(str) = parse_input()) -> None:
    oxygen = get_rating(gamma, inp)
    scrubber = get_rating(epsilon, inp, True)
    result = int(oxygen, 2) * int(scrubber, 2)
    print(f"Answer 2: {result}")


g, e = solve1()
solve2(g, e)
