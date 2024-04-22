from __future__ import annotations
from pathlib import Path
from time import perf_counter
import re

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]


def solve(data: list[str], result: int = 0, part1=True) -> int:
    max_red = 12
    max_green = 13
    max_blue = 14
    games_possible = []
    games_played = []
    for i, instruction in enumerate(data):
        game = i + 1
        possible = True
        inst = re.sub(r'Game \d+: ', '', instruction)
        sets = [x.strip().split(', ') for x in inst.split(';')]
        max_game_red = 0
        max_game_green = 0
        max_game_blue = 0
        for _set in sets:
            for cubes in _set:
                amount, color = cubes.split(' ')
                if color == 'red':
                    if int(amount) > max_red:
                        possible = False
                    max_game_red = int(amount) if int(amount) > max_game_red else max_game_red
                elif color == 'green':
                    if int(amount) > max_green:
                        possible = False
                    max_game_green = int(amount) if int(amount) > max_game_green else max_game_green
                elif color == 'blue':
                    if int(amount) > max_blue:
                        possible = False
                    max_game_blue = int(amount) if int(amount) > max_game_blue else max_game_blue
        if possible:
            games_possible.append((game, max_game_red, max_game_green, max_game_blue))
        games_played.append((game, max_game_red, max_game_green, max_game_blue))
    if part1:
        return sum([x[0] for x in games_possible])
    for game in games_played:
        product = game[1] * game[2] * game[3]
        result += product
    return result


timing_1 = perf_counter()
answer_1 = solve(test)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
