from __future__ import annotations
from pathlib import Path
from time import perf_counter
import numpy as np

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[list[int]]:
    with open(txt_file, 'r') as f:
        return [[int(x) for x in y] for y in f.read().split('\n')]


inp = parse_input()
test = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
]


def mark_visible(matrix, eye=None) -> np.ndarray:
    for i, row in enumerate(matrix):
        cur_height = -1
        for pos, height in enumerate(row):
            if i == 0:
                eye[i][pos] = 1
            elif height > cur_height:
                eye[i][pos] = 1
                cur_height = height
    return eye


def mark_p2(matrix, eye=None, old_scores=False) -> np.ndarray:
    for i, row in enumerate(matrix):
        for j, height in enumerate(row):
            if old_scores:
                score = 0
            else:
                score = eye[i][j]
            count = 0
            if 0 < i < (matrix.shape[0]-1):
                for right in row[j+1:]:
                    count += 1
                    if right < height:
                        continue
                    else:
                        break
            if count > 0:
                if not old_scores:
                    score = 1
                score *= count
                count = 0
                if j > 0:
                    for left in row[j-1::-1]:
                        count += 1
                        if left < height:
                            continue
                        else:
                            break
                score *= count
            eye[i][j] = score
    return eye


def solve(data: list[list[int]], result: int = 0, part1=True) -> int:
    mat = np.array(data)
    eye = np.zeros(mat.shape)
    if part1:
        for _ in range(2):
            eye = mark_visible(mat, eye)
            eye = mark_visible(np.fliplr(mat), np.fliplr(eye))
            eye = np.fliplr(eye)
            eye = eye.transpose()
            mat = mat.transpose()
        return np.count_nonzero(eye)
    eye = mark_p2(mat, eye)
    eye = eye.transpose()
    mat = mat.transpose()
    eye = mark_p2(mat, eye, old_scores=True)
    eye = eye.transpose()
    return eye.max()


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
