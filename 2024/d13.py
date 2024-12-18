from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any
import re
import functools


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


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, "r") as f:
        return f.read().split("\n\n")


inp = parse_input()
test = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split(
    "\n\n"
)


def find_optimal_cost(target_x, target_y, line1_dx, line1_dy, line2_dx, line2_dy):
    max_steps = max(abs(target_x // min(line1_dx, line2_dx)), abs(target_y // min(line1_dy, line2_dy))) + 1
    best_solution = None
    min_cost = float("inf")

    for steps1 in range(max_steps):
        for steps2 in range(max_steps):
            x = steps1 * line1_dx + steps2 * line2_dx
            y = steps1 * line1_dy + steps2 * line2_dy
            cost = steps1 * 3 + steps2
            if cost >= min_cost:
                break
            if x == target_x and y == target_y:
                min_cost = cost
                best_solution = (cost, steps1, steps2)

    return best_solution


@timer
def solve1(data: list[str], result: int = 0) -> int:
    tests = [[y for y in x.split("\n")] for x in data]
    pat = r"X.(\d+)\, Y.(\d+)"
    coins = 0
    i = 0
    for a, b, prize in tests:
        i += 1
        ax, ay = map(int, re.findall(pat, a)[0])
        bx, by = map(int, re.findall(pat, b)[0])
        px, py = map(int, re.findall(pat, prize)[0])
        solution = find_optimal_cost(px, py, ax, ay, bx, by)
        if solution:
            cost = solution[0]
            print(f"Machine {i} has optimal cost {cost}")
            coins += cost

    return coins


@timer
def solve2(data: list[str], result: int = 0) -> int:
    return result


answer_1 = solve1(inp)
answer_2 = solve2(inp)
