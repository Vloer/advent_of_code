from __future__ import annotations
from pathlib import Path

input_file = Path(__file__).parent / "inputs" / "d8.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()
test_set = [
    'acedgfb cdfbe gcdfa fbcad bda cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
test_set2 = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
             'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
             'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
             'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
             'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea']


def check(big: list[str], small: list[str]) -> bool:
    return all(x in big for x in small)


def decode(digits_in: str) -> dict(str, list[str]):
    poss = {}
    numbers = digits_in.split()
    for codestring in numbers:
        code = [x for x in codestring]
        if len(code) == 2:
            poss[1] = ''.join(code)
        elif len(code) == 3:
            poss[7] = ''.join(code)
        elif len(code) == 4:
            poss[4] = ''.join(code)
        elif len(code) == 7:
            poss[8] = ''.join(code)
    diff_4 = list(set(poss[4]).difference(poss[1]))
    for codestring in numbers:
        code = [x for x in codestring]
        if len(code) == 5:  # 2, 3, 5
            if check(code, poss[1]):
                poss[3] = ''.join(code)
            elif check(code, diff_4):
                poss[5] = ''.join(code)
            else:
                poss[2] = ''.join(code)
        elif len(''.join(code)) == 6:  # 0, 6, 9
            if check(code, poss[4]):
                poss[9] = ''.join(code)
            elif check(code, poss[1]):
                poss[0] = ''.join(code)
            else:
                poss[6] = ''.join(code)
    result = {poss[k]: k for k in poss}  # reverse keys and values
    return result


def get_output_value(decode_key: dict, digits_out: str) -> int:
    result = ''
    for code in digits_out.split():
        for k, v in decode_key.items():
            a = [x for x in code]
            b = [y for y in k]
            if check(a, b) and len(a) == len(b):
                result += str(v)
    return int(result)


def solve1(inp: str) -> int:
    result = 0
    check = [2, 4, 3, 7]
    for line in inp:
        digits_in, digits_out = line.split("|")
        digits_out = [x for x in digits_out.split()]
        unique_digits = sum(
            [[len(x) for x in digits_out].count(y) for y in check])
        result += unique_digits
    return result


def solve2(inp: str) -> int:
    result = 0
    for line in inp:
        digits_in, digits_out = line.split("|")
        poss = decode(digits_in)
        a = get_output_value(poss, digits_out)
        print(a)
        result += a
    return result


print(f"Answer 1: {solve1(inp)}")
print(f"Answer 2: {solve2(inp)}")


# def decode(poss: dict(str, list[str])) -> list[str]:
#     ans = {}
#     letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#     for k in letters:
#         ans[k] = []

#     # sort dict by key length
#     newlist = poss.items()
#     sortedlist = sorted(newlist, key=lambda s: len(s[0]))

#     # Extract all possible letters per capital letter
#     for k, v in sortedlist:
#         for uppercase in k:
#             if not len(ans[uppercase]):
#                 for val in v:
#                     for lowercase in val:
#                         if lowercase not in ans[uppercase]:
#                             ans[uppercase].append(lowercase)
