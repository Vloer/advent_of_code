from __future__ import annotations
from pathlib import Path
from time import perf_counter
from typing import Generator, List, Tuple, Any

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


SYMBOLS = '!@#$%^&*()/[]{}-='
inp = parse_input()
test = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]


def _symbol_in_row(row) -> Generator[int]:
    yield [i for i, c in enumerate(row) if c in SYMBOLS]


def get_symbol_locations(data) -> list[tuple[Any, int]]:
    locations = []
    for i, row in enumerate(data):
        for symbol in _symbol_in_row(row):
            locations.append(symbol)
    return locations

def decode_data(data) -> list[list[str]]:
    decoded = []
    for row in data:
        l = []
        for c in row:
            if c.isdigit():
                l.append(int(c))
            elif c == '.':
                l.append('dot')
            else:
                l.append('sym')
        decoded.append(l)
    return decoded

def check_adj(num: str, locations: list[list[int]])


def solve(data: list[str], result: int = 0, part1=True) -> int:
    locations = get_symbol_locations(data)
    decoded = decode_data(data)

    for row in data:
        num = ''
        restart_num = False
        for c in row:
            if c.isdigit():
                num += c
                continue
            if c == '.':
                if num != '':


    return result


timing_1 = perf_counter()
answer_1 = solve(test)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
