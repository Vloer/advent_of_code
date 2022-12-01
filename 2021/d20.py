from __future__ import annotations
from pathlib import Path
from time import perf_counter
from typing import Generator
import numpy as np

input_file = Path(__file__).parent / "inputs" / "d20.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n\n"))


inp = parse_input()
inp[1] = inp[1].split('\n')
test = [["..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"],
        [
    "#..#.",
    "#....",
    "##..#",
    "..#..",
    "..###"
]]


def create_input_image(data: list) -> np.array:
    if any(['#' in x for x in data]):
        original = np.array([[y == '#' for y in x] for x in data], dtype=int)
    else:
        original = data
    base = np.zeros(
        (np.shape(original)[0] + 4, np.shape(original)[1] + 4), dtype=int)
    base[2:np.shape(base)[0]-2, 2:np.shape(base)[1]-2] = original
    return base


def neighbours(matrix: np.array, pos: tuple(int)) -> Generator:
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    for i in range(max(0, pos[0] - 1), min(rows, pos[0] + 2)):
        for j in range(max(0, pos[1] - 1), min(cols, pos[1] + 2)):
            yield matrix[i][j]


def get_pixel_value(grid: np.array, pos: tuple(int)) -> int:
    num = list(neighbours(grid, pos))
    return int(''.join(str(x) for x in num), 2)


def create_output_image(input_image: np.array, algorithm: np.array) -> np.array:
    image = np.zeros_like(input_image)
    for x in range(1, np.shape(image)[0] - 1):
        for y in range(1, np.shape(image)[1] - 1):
            value = get_pixel_value(input_image, (y, x))
            image[y, x] = algorithm[value]
    return image


def shrink_output_image(image: np.array, shrink: int) -> np.array:
    return image[shrink:np.shape(image)[0]-shrink, shrink:np.shape(image)[1]-shrink]


def solve(data: list[int], result: int = 0, part1=True) -> int:
    algorithm = np.array([x == '#' for x in ''.join(data[0])], dtype=int)
    output_image = data[1]
    for i in range(2):
        input_image = create_input_image(output_image)
        output_image = create_output_image(input_image, algorithm)
    shrunk = shrink_output_image(output_image, i+1)
    result = np.sum(shrunk)
    return result


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(test, part1=False)
print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
