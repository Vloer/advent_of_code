from __future__ import annotations
from pathlib import Path
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = [
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
]


def solve(data: list[str] | str, result: int = 0, part1=True) -> int:
    if part1:
        max_len = 4
    else:
        max_len = 14
    if not isinstance(data, list):
        data = [data]
    for word in data:
        packet = ''
        for i, char in enumerate(word):
            packet += char
            if len(packet) == max_len:
                if len(set(packet)) == max_len:
                    return i+1
                else:
                    packet = packet[1:]

    return result


timing_1 = perf_counter()
for i in test:
    answer_1 = solve(i)
    print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
