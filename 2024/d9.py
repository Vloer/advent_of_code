from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any, NamedTuple
import functools
from collections import deque
from copy import deepcopy
from dataclasses import dataclass


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute and returned {result}")
        return result

    return wrapper


input_file = Path(__file__).parent / "inputs" / f"{Path(__file__).stem}.txt"


def parse_input(txt_file: str = input_file) -> str:
    with open(txt_file, "r") as f:
        return f.read()


inp = parse_input()
test = """2333133121414131402"""


def create_list(data):
    id = 0
    s = deque()
    pos = 0
    for i, n in enumerate(data):
        if i % 2 == 0:
            for _ in range(int(n)):
                s.append((str(id), pos))
                pos += 1
            id += 1
        else:
            for _ in range(int(n)):
                s.append((".", pos))
                pos += 1
    return s


@timer
def solve1(data: str, result: int = 0) -> int:
    final = []
    s = create_list(data)
    ss = deepcopy(s)
    for x, pos in reversed(ss):
        if x == ".":
            continue
        while s and s[0][0] != ".":
            n, _ = s.popleft()
            if pos < len(final):
                break
            final.append(n)
        if pos < len(final):
            break
        s.popleft()
        final.append(x)
        # print(''.join(final))

    for id, n in enumerate(final):
        result += id * int(n)
    return result


@dataclass
class Block:
    id: str
    start: int
    length: int


@timer
def solve2(data: str, result: int = 0) -> int:
    final = []
    s = deque()
    id_blocks = deque()
    spaces = deque()
    id = 0
    pos = 0
    for i, n in enumerate(data):
        if i % 2 == 0:
            id_blocks.append(Block(str(id), pos, int(n)))
            for _ in range(int(n)):
                s.append((str(id), pos))
                pos += 1
            id += 1
        else:
            spaces.append(Block(".", pos, int(n)))
            for _ in range(int(n)):
                s.append((".", pos))
                pos += 1

    id_blockss = deepcopy(id_blocks)
    for b in reversed(id_blockss):
        for space in spaces:
            if b.start < space.start:
                break
            if b.length <= space.length:
                space.length -= b.length
                b.start = space.start
                space.start += b.length
                id_blocks.append(b)
                if space.length == 0:
                    spaces.remove(space)
                break
        final.append(b)
    for b in final:
        for i in range(b.length):
            s = int(b.id) * (b.start + i)
            result += s

    return result


answer_1 = solve1(inp)
answer_2 = solve2(inp)
