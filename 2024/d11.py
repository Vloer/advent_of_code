from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any, Optional
import functools
from copy import deepcopy
import math
from collections import deque


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


input_file = Path(__file__).parent / "inputs" / f"{Path(__file__).stem}.txt"


def parse_input(txt_file: str = input_file) -> str:
    with open(txt_file, "r") as f:
        return f.read()


inp = parse_input()
test = """125 17"""


@functools.lru_cache(maxsize=None)
def calculate(n: int, remaining_blinks: int, total: Optional[int] = None) -> int:
    if total is None:
        total = 0
    if remaining_blinks == 0:
        total += 1
        return total
    if n == 0:
        return calculate(1, remaining_blinks - 1, total)
    length = int(math.log10(n)) + 1
    if length % 2 == 0:
        left = n // (1 * 10 ** (length // 2))
        right = n % (1 * 10 ** (length // 2))
        return calculate(left, remaining_blinks - 1, total) + calculate(right, remaining_blinks - 1, total)
    return calculate(n * 2024, remaining_blinks - 1, total)


@timer
def solve(data: str, blinks: int) -> int:
    stones = [int(n) for n in data.strip().split()]
    final = 0
    for n in stones:
        final += calculate(n, blinks)
    return final


answer_1 = solve(inp, 25)
answer_2 = solve(inp, 75)
