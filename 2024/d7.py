from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any
import functools
import itertools


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute and returned {result}")
        return result

    return wrapper


input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = """156: 15 6
190: 10 19
3267: 81 40 27
292: 11 6 16 20
7290: 6 8 6 15
192: 17 8 14""".split('\n')


def get_combinations(operators, length) -> set[tuple[str, ...]]:
    c = list(itertools.combinations_with_replacement(operators, length))
    operators.reverse()
    c += list(itertools.combinations_with_replacement(operators, length))
    return set(c)


@timer
def solve1(data: list[str], result: int = 0) -> int:
    operators = [
        '*', '+'
    ]
    for row in data:
        is_valid = False
        row_result, nums = row.split(': ')
        numbers = nums.split(' ')
        combinations = itertools.product(operators, repeat=len(numbers) - 1)
        for i, c in enumerate(combinations):
            string_to_eval = ''
            for j, n in enumerate(numbers):
                string_to_eval += n
                string_to_eval = str(eval(string_to_eval))
                try:
                    string_to_eval += c[j]
                except IndexError:
                    ...
            if int(string_to_eval) == int(row_result):
                is_valid = True
            if is_valid:
                break
        if is_valid:
            result += int(row_result)

    return result


@timer
def solve2(data: list[str], result: int = 0) -> int:
    operators = [
        '*', '+', '||'
    ]
    for r, row in enumerate(data):
        is_valid = False
        row_result, nums = row.split(': ')
        numbers = nums.split(' ')
        combinations = itertools.product(operators, repeat=len(numbers) - 1)
        for i, c in enumerate(combinations):
            string_to_eval = ''
            for j, n in enumerate(numbers):
                string_to_eval = str(eval(string_to_eval + n))
                if int(string_to_eval) > int(row_result):
                    break
                try:
                    operator = c[j]
                    if operator != '||':
                        string_to_eval += c[j]
                except IndexError:
                    ...

            if string_to_eval == row_result:
                is_valid = True
            if is_valid:
                break
        if is_valid:
            result += int(row_result)
    return result


#
answer_1 = solve1(test)
answer_2 = solve2(inp)
