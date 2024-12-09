from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any
import functools


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute")
        return result

    return wrapper


input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = """""".split('\n')


def solve(data: list[str], result: int = 0, part1=True) -> int:
    return result


answer_1 = solve(test)
print(f"Answer 1: {answer_1}")
answer_2 = solve(test, part1=False)
print(f"Answer 2: {answer_2}")
