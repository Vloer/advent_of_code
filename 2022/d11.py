from __future__ import annotations
from pathlib import Path
from time import perf_counter
from collections import deque
from typing import Callable, Optional

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()


class Monkey:
    def __init__(self, starting_items: list[int], operation: Callable, divisible_by: int):
        self.items = deque()
        self.operation = operation
        self.test = divisible_by
        self.test_true: Optional[Monkey] = None
        self.test_false: Optional[Monkey] = None
        self.throw_target: Optional[Monkey] = None
        self.inspects = 0
        self.divide_worry_level = 3
        [self.items.append(x) for x in starting_items]

    def inspect(self, item):
        self.inspects += 1
        item = self.operation(item)
        item //= self.divide_worry_level
        if item % self.test == 0:
            self.throw_target = self.test_true
        else:
            self.throw_target = self.test_false
        return item

    def receive(self, item):
        self.items.append(item)

    def take_item(self):
        return self.items.popleft()

    def do_turn(self):
        while self.items:
            item = self.take_item()
            item = self.inspect(item)
            self.throw_target.receive(item)


def create_test_data():
    m0 = Monkey([79, 98], lambda x: x * 19, 23)
    m1 = Monkey([54, 65, 75, 74], lambda x: x + 6, 19)
    m2 = Monkey([79, 60, 97], lambda x: x * x, 13)
    m3 = Monkey([74], lambda x: x + 3, 17)
    m0.test_true = m2
    m0.test_false = m3
    m1.test_true = m2
    m1.test_false = m0
    m2.test_true = m1
    m2.test_false = m3
    m3.test_true = m0
    m3.test_false = m1

    return [m0, m1, m2, m3]


def create_data():
    m0 = Monkey([71, 86], lambda x: x * 13, 19)
    m1 = Monkey([66, 50, 90, 53, 88, 85], lambda x: x + 3, 2)
    m2 = Monkey([97, 54, 89, 62, 84, 80, 63], lambda x: x + 6, 13)
    m3 = Monkey([82, 97, 56, 92], lambda x: x + 2, 5)
    m4 = Monkey([50, 99, 67, 61, 86], lambda x: x * x, 7)
    m5 = Monkey([61, 66, 72, 55, 64, 53, 72, 63], lambda x: x + 4, 11)
    m6 = Monkey([59, 79, 63], lambda x: x * 7, 17)
    m7 = Monkey([55], lambda x: x + 7, 3)

    m0.test_true = m6
    m0.test_false = m7
    m1.test_true = m5
    m1.test_false = m4
    m2.test_true = m4
    m2.test_false = m1
    m3.test_true = m6
    m3.test_false = m0
    m4.test_true = m5
    m4.test_false = m3
    m5.test_true = m3
    m5.test_false = m0
    m6.test_true = m2
    m6.test_false = m7
    m7.test_true = m2
    m7.test_false = m1

    return [m0, m1, m2, m3, m4, m5, m6, m7]


def solve(data: list[Monkey], result: int = 0, part1=True) -> int:
    if not part1:
        for monkey in data:
            monkey.divide_worry_level = 1
        for i in range(500):
            [monkey.do_turn() for monkey in data]
            # print(f'Round {i} done')
    else:
        for i in range(20):
            [monkey.do_turn() for monkey in data]
            # print(f'Round {i} done')
    inspects = [monkey.inspects for monkey in data]
    inspects.sort()
    try:
        result = inspects[-1] * inspects[-2]
    except IndexError:
        ...
    return result


timing_1 = perf_counter()
answer_1 = solve(create_test_data())
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(create_test_data(), part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
