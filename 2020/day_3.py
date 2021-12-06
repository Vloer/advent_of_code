#!python3

import os
import csv

ROOT = "C:\\Users\\RuweBo01\\Anaconda3\\Scripts\\Advent of code"
input_filee = "3_input.txt"
input_file = os.path.join(ROOT, input_filee)

with open(input_file, newline='\n') as csvfile:
    l = csv.reader(csvfile)
    inp = []
    for row in l:
        inp.append(', '.join(row))
inp = list(map(str, inp))

def create_new_field():
    # initialize input list
    complete_field = []
    amount_to_repeat = 1000  # 1 for none
    for row in inp:
        row = row * amount_to_repeat
        complete_field.append(list(row))

    row0 = col0 = 0  # starting position
    obj = {'matrix': complete_field,
           'cur_row': row0,
           'cur_col': col0}
    return(obj)


def get_mark(m, row, col):
    val = m[row][col]
    if val == ".":
        mark = "O"
    elif val == "#":
        mark = "X"
    else:
        raise TypeError(
            'Something went wrong while placing mark (most likely another mark is already in place)')
    return(mark)


def place_mark(m, row, col, placed_mark, print_results=True):
    m[row][col] = placed_mark
    if print_results:
        print(f"Placed '{placed_mark}' on [{row},{col}]")
    return(m)


def move(obj, row, col):
    # obj = object that contains matrix and current coordinates
    # row = how many steps to move in row direction
    # col = how many steps to move in col direction
    # Set value to O if its not a tree, X if it is a tree
    m = obj['matrix']
    row0 = obj['cur_row']
    col0 = obj['cur_col']

    row_new = row0 + row
    col_new = col0 + col

    mark_to_place = get_mark(m, row_new, col_new)
    m = place_mark(m, row_new, col_new, mark_to_place, False)

    obj['matrix'] = m
    obj['cur_row'] = row_new
    obj['cur_col'] = col_new
    return(obj)

def count_occurences(m, char):
    count = 0
    for row in m:
        count += row.count(char)
    return(count)

def traverse(obj, move_row, move_col):
    max_iter = 10000
    start_iter = 1

    num_rows = len(obj['matrix'])
    num_cols = len(obj['matrix'][0])
    # print(f"Size of object is {num_rows}*{num_cols}")

    while obj['cur_row'] < num_rows-1 and obj['cur_col'] < num_cols-1:
        obj = move(obj, move_row, move_col)
        start_iter += 1
        if start_iter == max_iter:
            print("max iter reached")
            break
    else:
        print(f"Edge of matrix reached at [{obj['cur_row']},{obj['cur_col']}]")

    occurences = count_occurences(obj['matrix'], "X")
    print(f"{occurences} trees hit for slope change [{move_row},{move_col}]")
    return(occurences)

total = 1
total *= traverse(create_new_field(), 1, 1)
total *= traverse(create_new_field(), 1, 3)
total *= traverse(create_new_field(), 1, 5)
total *= traverse(create_new_field(), 1, 7)
total *= traverse(create_new_field(), 2, 1)
print(total)
