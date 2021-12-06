#!python3 

from typing import List, Dict, Union
import os
import re

test = "FBFBBFFRLR"

ROOT = "C:\\Users\\RuweBo01\\Anaconda3\\Scripts\\Advent of code"
input_filee = "5_input.txt"
input_file = os.path.join(ROOT, input_filee)

def parse_input(txt_file: str = input_file) -> List[str]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))

cols = range(8)
rows = range(128)

def halve(letter: str, start: range) -> range:
    if letter in ["F", "L"]:
        return(start[:len(start)//2])
    if letter in ["B", "R"]:
        return(start[len(start)//2:])

def get_all_seat_ids(input_code: List[str], rows: range, cols: range) -> List[int]:
    output = []
    for seat in input_code:
        row_code = seat[:7]
        col_code = seat[7:]
        row = rows
        col = cols
        for letter in row_code:
            row = halve(letter, row)
        for letter in col_code:
            col = halve(letter, col)
        
        id = int(row[0]) * 8 + int(col[0])
        output.append(id)
    return(output)

def assignment_1():
    all_seats = get_all_seat_ids(parse_input(), rows, cols)
    return(max(all_seats))

def assignment_2():
    all_seats = get_all_seat_ids(parse_input(), rows, cols)
    for id in range(min(all_seats), max(all_seats):
        if id not in all_seats:
            if id + 1 in all_seats and id - 1 in all_seats:
                return(id)
    


print(assignment_1())
print(assignment_2())

