from __future__ import annotations
from pathlib import Path

input_file = Path(__file__).parent / "inputs" / "d8.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()
test_set = [['acedgfb', 'cdfbe','gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab', '|', 'cdfeb', 'fcadb', 'cdfeb', 'cdbaf']]
test_set2 = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

def solve_line(line: list[str]):
    '''
    Letter coding (each letter corresponds to a line on the display):
        AAA
       B   C
        DDD
       E   F
        GGG  
    num0 = "ABCEFG"
    num1 = "CF"
    num2 = "ACDEG"
    num3 = "ACDFG"
    num4 = "BCDF"
    num5 = "ABDFG"
    num6 = "ABDEFG"
    num7 = "ACF"
    num8 = "ABCDEFG"
    num9 = "ABCDFG"
    '''
    numbers = ["ABCEFG","CF","ACDEG","ACDFG","BCDF","ABDFG","ABDEFG","ACF","ABCDEFG","ABCDFG"]
    

def solve1(inp: list[list[str]]) -> None:
    result = 0
    check = [2, 4, 3, 7]
    for line in inp:
        digits_in, digits_out = line.split("|")
        digits_out = [x for x in digits_out.split()]
        unique_digits = sum([[len(x) for x in digits_out].count(y) for y in check])
        result += unique_digits
    return result


def solve2(inp: list[str]) -> None:
    result = 0
    return result


print(f"Answer 1: {solve1(inp)}")
print(f"Answer 2: {solve2(inp)}")