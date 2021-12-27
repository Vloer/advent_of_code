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
t1 = '[[[[[9,8],1],2],3],4]'
t2 = '[7,[6,[5,[4,[3,2]]]]]'
t3 = '[[6,[5,[4,[3,2]]]],1]'
t4 = '[[[[0,7],4],[15,[0,13]]],[1,1]]'
t5 = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
t6 = '[[[[0,7],4],[[7,8],0],[6,7]]]],[1,1]]'


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
    print(s)
    return s


def find_deepest(s: str):
    pat = re.compile(r'\[\d,\d\]')
    return pat.search(s)[0]


def explode(s: str):
    l = [x for x in s]
    loc = depth(s)[1]
    left_num = int(s[loc + 1])
    right_num = int(s[loc + 3])

    # Get first number to the left
    i = 1
    while i < loc:
        c = l[loc-i]
        if c not in ['[', ']', ',']:  # is number
            l[loc-i] = str(int(c) + left_num)
            break
        i += 1

    # Change first number to the left
    j = 5
    while loc + j < len(s):
        c = l[loc+j]
        if c not in ['[', ']', ',']:
            l[loc+j] = str(int(c) + right_num)
            break
        j += 1
    l = ''.join(l)

    # Replace deepest nest with 0
    s = l[:loc] + '0' + l[loc+5:]
    if depth(s)[0] > 4:
        s = explode(s)
    print(s)
    return s


def reduce(s: str) -> str:
    s = explode(s)
    s = split(s)
    d = depth(s)[0]
    if d > 4:
        s = reduce(s)

    return s


def solve(data: list[str], result: int = 0, part1=True) -> int:
    prev = data[0]
    for row in data[1:]:
        num = [eval(prev), eval(row)]

    return result


def test_func(s: str):
    # x = List(eval(l))
    # print(x.data)
    # x = reduce(s)
    x = reduce(s)
    print(x)
    return


# test_func(t1)
test_func(t5)
# test_func(t3)

# timing_1 = perf_counter()
# answer_1 = solve(test)
# print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
# timing_2 = perf_counter()
# answer_2 = solve(inp, part1=False)
# print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
