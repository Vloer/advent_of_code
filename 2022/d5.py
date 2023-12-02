from __future__ import annotations
from pathlib import Path
from time import perf_counter
import pprint

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'
pp = pprint.PrettyPrinter(indent=4)


def parse_input(txt_file: str = input_file) -> tuple[list[list[str]], list[str]]:
    with open(txt_file, 'r') as f:
        textsplit = f.read().split("\n\n")
        crane, commands = [x.split('\n') for x in textsplit]
        stack = []
        for i, row in enumerate(crane[::-1]):
            for col, col_letter in enumerate(range(1, len(row), 4)):
                if i == 0:
                    stack.append([])
                else:
                    letter = row[col_letter]
                    if letter != ' ':
                        stack[col].append(letter)
        return stack, commands


def parse_command(command: str) -> list[int, int, int]:
    return [int(s) for s in command.split() if s.isdigit()]


def get_last_letters(col: list[str], amount: int) -> tuple[list[str], list[str]]:
    all_letters = list(filter(None, col))
    last_letters = all_letters[-amount:]
    new_letters = all_letters[:-amount]
    return new_letters, last_letters


def place_letters(col: list[str], letters: list[str], part1) -> list[str]:
    if part1:
        return col + letters[::-1]
    return col + letters


inp, commands = parse_input()
test_stack = [['Z', 'N', ''], ['M', 'C', 'D'], ['P', '', '']]
test_commands = [
    'move 1 from 2 to 1',
    'move 3 from 1 to 3',
    'move 2 from 2 to 1',
    'move 1 from 1 to 2'
]


def solve(part1=True) -> str:
    stack, commands = parse_input()
    for _command in commands:
        command = parse_command(_command)
        amount, start, end = command
        start_col, letters = get_last_letters(stack[start - 1], amount)
        end_col = place_letters(stack[end - 1], letters, part1)
        stack[start - 1] = start_col
        stack[end - 1] = end_col
    word = []
    for col in stack:
        word += col[-1] if col else ' '
    return ''.join(word)


timing_1 = perf_counter()
answer_1 = solve(part1=True)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
