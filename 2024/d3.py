from __future__ import annotations
from pathlib import Path
from time import perf_counter
import re

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> str:
    with open(txt_file, 'r') as f:
        return f.read()


inp = parse_input()
test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def solve(data: str, result: int = 0, part1=True) -> int:
    pat = r'mul\(\d+\,\d+\)'
    matches = re.findall(pat, data)
    s = 0
    for match in matches:
        pat = r'\((\d+)\,(\d+)\)'
        num1, num2 = re.findall(pat, match)[0]
        s += (int(num1) * int(num2))
    return s


def solve2(data: str, result: int = 0, part1=True) -> int:
    pat = r'(?:mul\((\d+\,\d+)\))|(don\'t\(\))|(do\(\))'
    matches = re.finditer(pat, data)
    count = True
    s = 0
    for match in matches:
        m = match[0]
        if m == 'do()':
            count = True
        elif m == 'don\'t()':
            count = False
        else:
            if count:
                pat = r'(\d+)\,(\d+)'
                num1, num2 = re.findall(pat, m)[0]
                s += (int(num1) * int(num2))
    return s


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve2(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
