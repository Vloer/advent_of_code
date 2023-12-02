from __future__ import annotations
from pathlib import Path
from time import perf_counter
import numpy as np
import pprint

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2'
]
test2 = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20'
]

def draw(visited, sh=50):
    square = np.zeros(shape=(sh,sh))
    for d in visited:
        x = d[1]+(sh/2)
        y = (sh/2)-d[0]
        square[int(y)][int(x)] = 1
    print(square)
    print(1)

def draw2(field, new_pos, symbol) -> list[str]:
    x = new_pos[1] + (len(field)/2)
    y = (len(field)/2) - new_pos[0]
    _new = list(field[int(y)])
    _new[int(x)] = symbol
    field[int(y)] = ''.join(_new)
    for row in field:
        print(row)
    print(' ')
    return field

def solve(data: list[str], result: int = 0, part1=True, field_size=30) -> int:
    snake_len = 1 if part1 else 9
    snake = [(0, 0)] * (snake_len + 1)
    visited = [(0, 0)]
    field = ['.'*field_size]*field_size
    for cmd in data:
        y, x = snake[0]  # head
        d, amt = cmd.split(' ')
        amt = int(amt)
        if d == 'R':
            for _ in range(amt):
                x = snake[0][1] + 1
                snake[0] = y, x
                field = draw2(field, snake[0], 'H')
                for body in range(1, len(snake)):
                    y_body, x_body = snake[body]
                    y, x = snake[body-1]
                    if abs(x - x_body) > 1:
                        if y_body != y:
                            y_body = y
                        x_body += 1
                        snake[body] = (y_body, x_body)
                        field = draw2(field, snake[body], str(body))
                    else:
                        break
                    if body == len(snake) - 1:
                        visited.append((y_body, x_body))
        elif d == 'L':
            for _ in range(amt):
                x = snake[0][1] - 1
                snake[0] = y, x
                for body in range(1, len(snake)):
                    y_body, x_body = snake[body]
                    y, x = snake[body - 1]
                    field = draw2(field, snake[body], str(body))
                    if abs(x - x_body) > 1:
                        if y_body != y:
                            y_body = y
                        x_body -= 1
                        snake[body] = (y_body, x_body)
                        field = draw2(field, snake[0], 'H')
                    else:
                        break
                    if body == len(snake) - 1:
                        visited.append((y_body, x_body))
        elif d == 'U':
            for _ in range(amt):
                y = snake[0][0] + 1
                snake[0] = y, x
                field = draw2(field, snake[0], 'H')
                for body in range(1, len(snake)):
                    y_body, x_body = snake[body]
                    y, x = snake[body - 1]
                    if abs(y - y_body) > 1:
                        if x_body != x:
                            x_body = x
                        y_body += 1
                        snake[body] = (y_body, x_body)
                        field = draw2(field, snake[body], str(body))
                    else:
                        break
                    if body == len(snake) - 1:
                        visited.append((y_body, x_body))
        elif d == 'D':
            for _ in range(amt):
                y = snake[0][0] - 1
                snake[0] = y, x
                field = draw2(field, snake[0], 'H')
                for body in range(1, len(snake)):
                    y_body, x_body = snake[body]
                    y, x = snake[body - 1]
                    if abs(y - y_body) > 1:
                        if x_body != x:
                            x_body = x
                        y_body -= 1
                        snake[body] = (y_body, x_body)
                        field = draw2(field, snake[body], str(body))
                    else:
                        break
                    if body == len(snake) - 1:
                        visited.append((y_body, x_body))
    # visited = set(visited)
    draw(visited)
    return len(visited)


timing_1 = perf_counter()
# answer_1 = solve(test)
# print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(test2, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
