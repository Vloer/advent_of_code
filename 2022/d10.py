from __future__ import annotations
from pathlib import Path
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test1 = ['noop',
         'addx 3',
         'addx -5']
test2 = ['addx 15',
         'addx -11',
         'addx 6',
         'addx -3',
         'addx 5',
         'addx -1',
         'addx -8',
         'addx 13',
         'addx 4',
         'noop',
         'addx -1',
         'addx 5',
         'addx -1',
         'addx 5',
         'addx -1',
         'addx 5',
         'addx -1',
         'addx 5',
         'addx -1',
         'addx -35',
         'addx 1',
         'addx 24',
         'addx -19',
         'addx 1',
         'addx 16',
         'addx -11',
         'noop',
         'noop',
         'addx 21',
         'addx -15',
         'noop',
         'noop',
         'addx -3',
         'addx 9',
         'addx 1',
         'addx -3',
         'addx 8',
         'addx 1',
         'addx 5',
         'noop',
         'noop',
         'noop',
         'noop',
         'noop',
         'addx -36',
         'noop',
         'addx 1',
         'addx 7',
         'noop',
         'noop',
         'noop',
         'addx 2',
         'addx 6',
         'noop',
         'noop',
         'noop',
         'noop',
         'noop',
         'addx 1',
         'noop',
         'noop',
         'addx 7',
         'addx 1',
         'noop',
         'addx -13',
         'addx 13',
         'addx 7',
         'noop',
         'addx 1',
         'addx -33',
         'noop',
         'noop',
         'noop',
         'addx 2',
         'noop',
         'noop',
         'noop',
         'addx 8',
         'noop',
         'addx -1',
         'addx 2',
         'addx 1',
         'noop',
         'addx 17',
         'addx -9',
         'addx 1',
         'addx 1',
         'addx -3',
         'addx 11',
         'noop',
         'noop',
         'addx 1',
         'noop',
         'addx 1',
         'noop',
         'noop',
         'addx -13',
         'addx -19',
         'addx 1',
         'addx 3',
         'addx 26',
         'addx -30',
         'addx 12',
         'addx -1',
         'addx 3',
         'addx 1',
         'noop',
         'noop',
         'noop',
         'addx -9',
         'addx 18',
         'addx 1',
         'addx 2',
         'noop',
         'noop',
         'addx 9',
         'noop',
         'noop',
         'noop',
         'addx -1',
         'addx 2',
         'addx -37',
         'addx 1',
         'addx 3',
         'noop',
         'addx 15',
         'addx -21',
         'addx 22',
         'addx -6',
         'addx 1',
         'noop',
         'addx 2',
         'addx 1',
         'noop',
         'addx -10',
         'noop',
         'noop',
         'addx 20',
         'addx 1',
         'addx 2',
         'addx 2',
         'addx -6',
         'addx -11',
         'noop',
         'noop',
         'noop']


class X:
    row_length = 40

    def __init__(self):
        self.cycle = 0
        self.value = 1
        self.intervals = []
        self.msg = ''

    @property
    def signal_strength(self):
        return self.cycle * self.value

    def add_cycle(self, amount):
        for _ in range(amount):
            self.cycle += 1
            self.check_cycle()

    def check_cycle(self):
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            print(f'After cycle {self.cycle} value is {self.value} with signal strength {self.signal_strength}')
            self.intervals.append(self.signal_strength)
        row_pos = self.cycle % 40 - 1
        char = '.'
        if row_pos == 0:
            self.msg += '\n'
        if row_pos in range(self.value-1, self.value+2):
            char = '#'
        self.msg += char

    def execute(self, val):
        self.add_cycle(2)
        self.value += val


def solve(instructions: list[str], result: int = 0, part1=True, x=X()) -> int:
    for inst in instructions:
        if inst == 'noop':
            x.add_cycle(1)
        else:
            val = int(inst[5:])
            x.execute(val)

    if part1:
        return sum(x.intervals)
    print(x.msg)


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
