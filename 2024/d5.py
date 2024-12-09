from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any
import functools
from collections import defaultdict


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
        return f.read().split("\n\n")


inp = parse_input()
test = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split('\n\n')


def order(data: list[str], rules: dict[str, list[str]]) -> list[str]:
    for i in range(len(data)):
        swapped = False
        for j in range(len(data) - 1):
            n1 = data[j]
            n2 = data[j + 1]
            if should_swap(n1, n2, rules):
                swapped = True
                data[j], data[j + 1] = data[j + 1], data[j]
        if not swapped:
            break
    return data


def should_swap(num1, num2, rules) -> bool:
    """Checks if num1 should be before num2"""
    return num1 in rules[num2]


@timer
def solve(data: list[str], result: int = 0, part1=True) -> int:
    _rules, tests = data
    rules = defaultdict(list)
    for rule in _rules.split('\n'):
        k, v = rule.split('|')
        rules[k].append(v)

    for t in tests.split('\n'):
        is_good = True
        nums = t.split(',')
        for i, n in enumerate(nums):
            remaining_numbers = nums[i + 1:]
            for r in remaining_numbers:
                if n in rules[r]:
                    is_good = False
                    break
            if not is_good:
                break
        if part1:
            if is_good:
                middle = nums[len(nums) // 2]
                result += int(middle)
        else:
            if not is_good:
                nums = order(nums, rules)
                middle = nums[len(nums) // 2]
                result += int(middle)

    return result


answer_1 = solve(inp)
print(f"Answer 1: {answer_1}")
answer_2 = solve(inp, part1=False)
print(f"Answer 2: {answer_2}")
