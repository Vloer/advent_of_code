from __future__ import annotations
from pathlib import Path
from time import perf_counter
import re

input_file = Path(__file__).parent / "inputs" / "d2.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


# inp = parse_input()
test = [
    '[1,2]',
    '[[1,2],3]',
    '[9,[8,7]]',
    '[[1,9],[8,5]]',
    '[[[[1,2],[3,4]],[[5,6],[7,8]]],9]',
    '[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]',
    '[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]'
]
t1 = [
'[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
'[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
'[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
'[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
'[7,[5,[[3,8],[1,4]]]]',
'[[2,[2,2]],[8,[8,1]]]',
'[2,9]',
'[1,[[[9,3],9],[[9,0],[0,7]]]]',
'[[[5,[7,4]],7],1]', 
'[[[[4,2],2],6],[8,7]]'
]


def depth(s: str) -> int | int:
    depth = 0
    max_depth = 0
    max_depth_start_location = None
    for i, letter in enumerate(s):
        if letter == '[':
            depth += 1
            if depth > max_depth:
                max_depth = depth
            if depth > 4 and not max_depth_start_location:
                max_depth_start_location = i
        elif letter == ']':
            depth -= 1
    return max_depth, max_depth_start_location


def get_deepest():
    return


class List:
    def __init__(self, data, parent=None, d=0):
        self.data = data
        self.data_final: List = None
        self.parent = parent
        self.children = []
        self.d = d
        self.explode2()
        if self.d == 3:
            if self.data_final.data == self.data[0]:
                self.data[1] += self.data[0][1]
                self.data[0] = 0
            elif self.data_final.data == self.data[1]:
                self.data[0] += self.data[1][0]
                self.data[1] = 0

    def explode2(self):
        if self.d != 4:
            for l in self.data:
                if isinstance(l, list):
                    self.children.append(l)
                    self.data_final = List(l, self.data, self.d+1)


def split(s: str) -> str:
    s_list = '[' + s.replace('[', '').replace(']', '') + ']'
    list_of_numbers = eval(s_list)
    for num in list_of_numbers:
        if num > 10:
            rounded = num // 2
            new_num = [rounded, rounded + 1]
            idx = s.index(str(num))
            s = s[:idx] + str(new_num).replace(' ', '') + s[idx+2:]
            list_of_numbers.remove(num)
            if any([x > 10 for x in list_of_numbers]):
                s = split(s)
            break
    return s


def explode(s: str):
    l = []
    continue_next = False
    for i, c in enumerate(s[1:]):
        if continue_next:
            continue_next = False
            continue
        if s[i] in ['[',']',',']:
            l.append(s[i])
        else:
            if c in ['[',']',',']:
                l.append(s[i])
            else:
                l.append(s[i]+c)
                continue_next = True
    

    loc = depth(s)[1]
    if not loc:
        return s
    loc_1 = loc_2 = loc
    left_num = int(l[loc + 1])
    right_num = int(l[loc + 3])

    # Get first number to the left
    i = 1
    while i < loc:
        c = l[loc-i]
        if c not in ['[', ']', ',']:  # is number
            res = int(c) + left_num
            l[loc-i] = str(res)
            if res > 10:
                loc_1 += 1
            break
        i += 1
    # Change first number to the left
    j = 5
    while loc + j < len(s):
        c = l[loc+j]
        if c not in ['[', ']', ',']:
            res = int(c) + right_num
            l[loc+j] = str(res)
            if res > 10:
                loc_2 += 1
            break
        j += 1
    l = ''.join(l)

    # Replace deepest nest with 0
    s = l[:loc_1] + '0' + l[loc_2+5:]
    if depth(s)[0] > 4:
        s = explode(s)
    return s


def reduce(s: str) -> str:
    s = explode(s)
    s = split(s)
    d = depth(s)[0]
    if d > 4:
        s = reduce(s)
    return s


def solve(data: list[str], result: int = 0, part1=True) -> int:
    num = data[0]
    for row in data[1:]:
        num_to_analyze = f'[{num},{row}]'
        num = reduce(num_to_analyze)
        print(num)

    return result


def test_func(s: str):
    # x = List(eval(l))
    # print(x.data)
    # x = reduce(s)
    x = reduce(s)
    print(x)
    return


solve(t1)

# timing_1 = perf_counter()
# answer_1 = solve(test)
# print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
# timing_2 = perf_counter()
# answer_2 = solve(inp, part1=False)
# print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
