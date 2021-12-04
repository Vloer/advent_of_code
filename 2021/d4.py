from __future__ import annotations
from pathlib import Path
import numpy as np

input_file = Path(__file__).parent / "inputs" / "d4.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()
numbers_drawn = list(map(int, inp[0].split(",")))
boards = []
new_board = []
for i in range(2, len(inp)):
    if inp[i] != "":
        new_board.append(list(map(int, inp[i].split())))
    else:
        boards.append(np.array(new_board))
        new_board = []


def check_board(b: np.array) -> bool:
    if any(b.sum(axis=0) == len(b) * 1000):
        return True
    return False



def solve1() -> None:
    result = 0
    for num in numbers_drawn:
        for board in boards:
            if num in board:
                y, x = np.where(board == num)
                board[y, x] = 1000
                if check_board(board):
                    print(board)
                    return board

    print(f"Answer 1: {result}")


def solve2() -> None:
    result = 0
    print(f"Answer 2: {result}")


solve1()
