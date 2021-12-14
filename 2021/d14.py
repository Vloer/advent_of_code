from __future__ import annotations
from pathlib import Path
from collections import defaultdict, Counter

input_file = Path(__file__).parent / "inputs" / "d14.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n\n")


def parse_input_final(data: list[str]) -> list[str] | defaultdict(list):
    template = data[0]
    rules = defaultdict()
    for rule in data[1].split("\n"):
        k, v = rule.split(' -> ')
        rules[k] = v
    return template, rules


inp = parse_input()
test1 = [
    'NNCB',

    '''CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''
]


def get_new_template_count(template: str, rules: defaultdict(str), steps: int) -> Counter:

    starting_pairs = [template[i-1:i+1] for i in range(1, len(template))]
    count = Counter()
    letter_count = Counter(template)
    [count.update({pair: 1}) for pair in starting_pairs]
    for _ in range(steps):
        update = Counter()
        for k, v in rules.items():
            if count[k] > 0:
                key1 = k[0] + v
                key2 = v + k[1]
                update.update({key1: count[k], key2: count[k]})
                letter_count.update({v: count[k]})
        count = update.copy()

    return letter_count


def solve(data: list[str], steps: int, result: int = 0) -> int:
    template, rules = parse_input_final(data)
    c = get_new_template_count(template, rules, steps)
    result = c.most_common(1)[0][1] - c.most_common()[-1][1]
    return result


print(f"Answer 1: {solve(inp, 10)}")
print(f"Answer 2: {solve(inp, 40)}")
