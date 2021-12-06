#!python3

"""
Testcase:
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

import csv

input_file = "2_input.txt"

with open(input_file, newline='\n') as csvfile:
    l = csv.reader(csvfile)
    inp = []
    for row in l:
        inp.append(', '.join(row))
inp = list(map(str, inp))


def parser(s):
    v = s.split(' ')  # ['1-3', 'a:', 'abcde']
    v_min = v[0].split('-')[0]
    v_max = v[0].split('-')[1]
    v_letter = v[1][0]
    v_pass = v[2]

    v_dict = {"min": v_min,
              "max": v_max,
              "letter": v_letter,
              "pass": v_pass}
    return(v_dict)

def check_1(s):
    count = s['pass'].count(s['letter'])
    if int(s['min']) <= count <= int(s['max']):
        return 1
    else:
        return 0

def check_2(s):
    pos1 = int(s['min']) - 1
    pos2 = int(s['max']) - 1
    test1 = test2 = 0
    if s['pass'][pos1] == s['letter']:
        test1 = 1
    if s['pass'][pos2] == s['letter']:
        test2 = 1
    
    if test1+test2 == 1:
        return 1
    else:
        return 0

def get_result(func):
    final = 0
    for case in inp:
        result = func(parser(case))
        final += result
    return(final)

print(get_result(check_2))