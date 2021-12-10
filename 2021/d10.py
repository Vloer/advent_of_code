from __future__ import annotations
from pathlib import Path
import statistics

input_file = Path(__file__).parent / "inputs" / "d10.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()
test_set = ['[({(<(())[]>[[{[]{<()<>>',
            '[(()[<>])]({[<{<<[]>>(',
            '{([(<{}[<>[]}>{[]{[(<()>',
            '(((({<>}<{<{<>}{[]{[]{}',
            '[[<[([]))<([[{}[[()]]]',
            '[{[{({}]{}}([{[{{{}}([]',
            '{<[[]]>}<{[{[{[]{()[[[]',
            '[<(<(<(<{}))><([]([]()',
            '<{([([[(<>()){}]>(<<{{',
            '<{([{{}}[<[[[<>{}]]]>[]]']

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores_corrupted = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores_incomplete = {')': 1, ']': 2, '}': 3, '>': 4}


def solve(data: list[str], part1=False) -> int:
    result = []
    if part1:
        result = 0
    for row in data:
        CORRUPTED = False
        score_line = 0
        open = []
        i = 0
        for symbol in row:
            i += 1
            if symbol in pairs:
                open.append(symbol)
            else:
                if symbol == pairs[open[-1]]:
                    open.pop()
                else:
                    if i != len(row):  # line corrupted
                        if part1:
                            result += scores_corrupted[symbol]
                        CORRUPTED = True
                        break
        if not part1 and not CORRUPTED:
            for symbol in open[::-1]:
                score_line *= 5
                score_line += scores_incomplete[pairs[symbol]]
            result.append(score_line)
    if part1:
        final_result = result
    else:
        final_result = statistics.median(result)

    return final_result


print(f"Answer 1: {solve(inp, True)}")
print(f"Answer 2: {solve(inp)}")
