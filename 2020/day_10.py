#!python3

from typing import List
import os

ROOT = "C:\\Users\\RuweBo01\\Anaconda3\\Scripts\\Advent of code"
input_filee = "10_input_test.txt"
input_file = os.path.join(ROOT, input_filee)


def parse_input(txt_file: str = input_file) -> List[int]:
    with open(txt_file, 'r') as f:
        return([int(x) for x in f.read().split("\n")])


def assignment_1(l: List[int]) -> int:
    l.append(0)
    l.append(max(l) + 3)
    l.sort()
    diff_1 = 0
    diff_3 = 0
    for i in range(1, len(l)):
        if (l[i] - l[i-1]) == 1:
            diff_1 += 1
        elif (l[i] - l[i-1]) == 3:
            diff_3 += 1
    return(diff_1 * diff_3)


def check_possibilities(l: List[int], max_diff: int = 3, printing: bool = False) -> int:
    total = 0
    for i in range(1, len(l)):
        if abs(l[0]-l[i]) <= max_diff:
            print(f"Checking {l[0]} and {l[i]}: correct") if printing else 0
            total += 1
        else:
            print(f"Checking {l[0]} and {l[i]}: false") if printing else 0
            break
    return total

def assignment_2(l: List[int], printing: bool = False) -> int:
    l.append(0)
    # l.append(max(l) + 3)
    l.sort(reverse=True)
    num_removed = 0

    print(l)
    for i in range(len(l)-2):
        if abs(l[i]-l[i+2]) < 3:
            print(f"{l[i+1]} can be removed")
            num_removed += 1

    return 2 ** num_removed


# print(assignment_1(parse_input()))
print(assignment_2(parse_input()))

'''
niks weg (possibility 1)
11 weg
6, 6+11 weg
5, 5+6, 5+11 5+6+11, weg
4, 4+5, 4+6, 4+11, 4+5+6, 4+5+11, 4+5+6+11, 4+6+11 weg

4 getallen kunnen weg, dus 2**4=16

2 ** num_removed - sum(2**(i-3) for i in range(3, num_removed+ 1))
'''