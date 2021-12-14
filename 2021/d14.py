from __future__ import annotations
from pathlib import Path
from collections import defaultdict, Counter
import functools
from frozendict import frozendict

input_file = Path(__file__).parent / "inputs" / "d14.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        # return([x.split("\n") for x in f.read().split("\n\n")])
        return f.read().split("\n\n")


def parse_input_final(data: list[str]) -> list[str] | defaultdict(list):
    # template = [char for char in data[0]]
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

def freezeargs(func):
    """Transform mutable dictionnary
    Into immutable
    Useful to be compatible with cache
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        args = tuple([frozendict(arg) if isinstance(arg, dict) else arg for arg in args])
        kwargs = {k: frozendict(v) if isinstance(v, dict) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapped

@freezeargs
@functools.lru_cache(maxsize=1)
def get_new_template(template: str, rules: defaultdict(str), steps: int) -> str:
    for _ in range(steps):
        template_pairs = []
        [template_pairs.append(template[i-1:i+1]) for i in range(1,len(template))]
        for i, pair in enumerate(template_pairs):
            template_pairs[i] = f"{pair[0]}{rules[pair]}"
        template_pairs.append(template[-1])
        template = ''.join(template_pairs)
        print(f"Completed step {_+1}, length is {len(template)}")
    return template


def solve(data: list[str], steps: int, result: int = 0) -> int:
    template, rules= parse_input_final(data)
    template = get_new_template(template, rules, steps)
    c = Counter(template)
    result = c.most_common(1)[0][1] - c.most_common()[-1][1]
    return result



# print(f"Answer 1: {solve(inp, 10)}")
print(f"Answer 2: {solve(inp, 40)}")

