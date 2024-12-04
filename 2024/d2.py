from __future__ import annotations
from pathlib import Path
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split('\n')
UNSAFE = []


def check_if_safe(nums: list[int], unsafe_removed: bool = False) -> bool:
    is_increasing = nums[1] > nums[0]
    if nums == [89, 92, 95, 93, 94, 97, 98] or nums == [78, 85, 88, 90, 92, 94, 96, 98]:
        print(1)
    for i in range(1, len(nums)):
        try:
            diff = nums[i] - nums[i - 1]

            if is_increasing:
                if not (1 <= diff <= 3):
                    if unsafe_removed:
                        return False
                    nums_copy = nums.copy()
                    del nums_copy[i]
                    return check_if_safe(nums_copy, True)
            else:
                if not (-3 <= diff <= -1):
                    if unsafe_removed:
                        return False
                    nums_copy = nums.copy()
                    del nums_copy[i]
                    return check_if_safe(nums_copy, True)
        except IndexError:
            pass

    return True


def check_if_safe_part1(nums: list[int]) -> bool:
    is_increasing = False
    for i in range(1, len(nums)):
        if i == 1:
            if nums[i] > nums[i - 1]:
                is_increasing = True
        diff = nums[i] - nums[i - 1]
        if is_increasing:
            if diff < 1 or diff > 3:
                return False
        else:
            if diff > -1 or diff < -3:
                return False
    return True


def solve(data: list[str], result: int = 0, part1=True) -> int:
    safe = 0
    for row in data:
        nums = list(map(int, row.split(' ')))
        if part1:
            if check_if_safe_part1(nums):
                safe += 1
        else:
            if check_if_safe(nums):
                # print(f'{row} is safe')
                safe += 1
            else:
                UNSAFE.append(list(map(int, row.split(' '))))
    return safe


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
