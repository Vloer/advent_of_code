#!python3

from typing import List, Dict, Union
import os

ROOT = "C:\\Users\\RuweBo01\\Anaconda3\\Scripts\\Advent of code"
input_filee = "6_input.txt"
input_file = os.path.join(ROOT, input_filee)

def parse_input(txt_file: str = input_file) -> List[str]:
    with open(txt_file, 'r') as f:
        return [line.split("\n") for line in f.read().split("\n\n")]

def assignment_1():
    sum = 0
    for group in parse_input():
        sum += len(set(''.join(map(str, group))))
    return sum

def assignment_2():
    sum = 0
    for large_group in parse_input():
        res = 0
        for letter in large_group[0]:
            if all([letter in group for group in large_group]):
                res += 1
        sum += res
    return sum

    
print(assignment_1())
print(assignment_2())