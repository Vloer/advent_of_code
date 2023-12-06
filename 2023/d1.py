from __future__ import annotations
from pathlib import Path
import re
from copy import deepcopy
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = [
    'onetwone',
    'four82nine74',
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]

digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
digits_replace2 = {
    'one': 'on@e',
    'two': 'tw@o',
    'three': 'th@ree',
    'four': 'fo@ur',
    'five': 'fi@ve',
    'six': 'si@x',
    'seven': 'se@ven',
    'eight': 'ei@ght',
    'nine': 'ni@ne',
}

digits_replace = {
    'one': 'oonee',
    'two': 'ttwoo',
    'three': 'tthreee',
    'four': 'ffourr',
    'five': 'ffivee',
    'six': 'ssixx',
    'seven': 'ssevenn',
    'eight': 'eeightt',
    'nine': 'nninee',
}

def replace_func(s: str) -> bool | str:
    while True:
        for k, v in digits.items():
            s_out = s.replace(k, str(v))
        if s == s_out:
            return s_out
        s_out = s
def solve(data: list[str], result: int = 0, part1=True) -> int:
    for r in data:
        if not part1:
            for k, v in digits.items():
                r = r.replace(str(v), k)
            for k, v in digits_replace.items():
                r = r.replace(k, v)
            r = replace_func(r)
            found_digits = []
            for k, v in digits_replace.items():
                found = re.findall(rf'{v}', r)
                found_digits += found
            digits_in_word = [(r.find(d), d) for d in digits.keys() if r.find(d) > -1]
            digits_in_word.sort()
            d1 = digits_in_word[0][1]
            d2 = digits_in_word[-1][1]
            res = int(str(digits.get(d1)) + str(digits.get(d2)))
            result += res
        if part1:
            l = [x for x in r if x.isdigit()]
            if l:
                result += int(str(l[0]) + str(l[-1]))
    return result


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(test, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
