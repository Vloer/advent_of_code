from __future__ import annotations
from pathlib import Path

input_file = Path(__file__).parent / "inputs" / "d2.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([int(x) for x in f.read().split(",")])


inp = parse_input()


def enter_code(input_list: list[int], code: list[int]) -> bool | list[int]:
    if code[0] == 1:
        input_list[code[3]] = input_list[code[1]] + input_list[code[2]]
    elif code[0] == 2:
        input_list[code[3]] = input_list[code[1]] * input_list[code[2]]
    elif code[0] == 99:
        return False
    return input_list


def solve1(inp=inp) -> None:
    inp[1] = 12
    inp[2] = 2
    codelist = [inp[i-4:i] for i in range(4, len(inp), 4)]
    for code in codelist:
        result = inp[0]
        inp = enter_code(inp, code)
        if not inp:
            break
    print(f"Answer 1: {result}")


def solve2(inp=inp) -> None:
    result = 0
    target = 19690720
    for noun in range(100):
        for verb in range(100):

    print(f"Answer 2: {result}")


solve1()
solve2()
