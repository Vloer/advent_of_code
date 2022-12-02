from __future__ import annotations
from pathlib import Path
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / "d2.txt"

# Y>A Z>B X>C
# B>X C>Y A>Z
scores = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
scores_2 = {'X': 0, 'Y': 3, 'Z': 6}
to_lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
to_draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
test = [
    'A Y',
    'B X',
    'C Z']


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()


def solve(data: list[str], result: int = 0, part1=True) -> int:
    if part1:
        result = 0
        for match in data:
            a, b = match.split(' ')
            score_choice = scores.get(b)
            if b == 'X':
                score_match = 6 if a == 'C' else 3 if a == 'A' else 0
            elif b == 'Y':
                score_match = 6 if a == 'A' else 3 if a == 'B' else 0
            elif b == 'Z':
                score_match = 6 if a == 'B' else 3 if a == 'C' else 0
            total_score = score_match + score_choice
            result += total_score
    else:
        result = 0
        for match in data:
            a, b = match.split(' ')
            score_match = scores_2.get(b)
            if score_match == 0:
                score_choice = scores.get(to_lose.get(a))
            elif score_match == 3:
                score_choice = scores.get(to_draw.get(a))
            elif score_match == 6:
                score_choice = scores.get(to_win.get(a))
            total_score = score_match + score_choice
            result += total_score
    return result


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
