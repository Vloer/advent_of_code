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
insert_number = 0
for i in range(2, len(inp)):
    if inp[i] != "":
        new_board.append(list(map(int, inp[i].split())))
    else:
        boards.append(np.array(new_board))
        new_board = []


def check_board(b: np.array) -> bool:
    if any(b.sum(axis=0) == len(b) * insert_number) or any(b.sum(axis=1) == len(b) * insert_number):
        return True
    return False


def play_bingo(boards: list[list[int]], numbers_drawn: list[int], part2=False) -> tuple(np.array, int):
    idx_to_skip = []
    for num in numbers_drawn:
        for i in range(len(boards)):
            if i not in idx_to_skip:
                board = boards[i]
                if num in board:
                    y, x = np.where(board == num)
                    board[y, x] = insert_number
                    if check_board(board):
                        if not part2:
                            return(board, num)
                        idx_to_skip.append(i)
                        last_board = board
                        last_num = num
    return(last_board, last_num)


def solve1(boards, numbers_drawn, part2) -> None:
    board, num = play_bingo(boards, numbers_drawn, part2)
    result = num * np.sum(board, where=(board != insert_number))
    print(f"Answer 1: {result}")


def solve2(boards, numbers_drawn, part2) -> None:
    board, num = play_bingo(boards, numbers_drawn, part2)
    result = num * np.sum(board, where=(board != insert_number))
    print(f"Answer 2: {result}")


# solve1(boards, numbers_drawn, False)
solve2(boards, numbers_drawn, True)