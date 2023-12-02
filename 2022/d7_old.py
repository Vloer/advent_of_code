from __future__ import annotations
from pathlib import Path
from time import perf_counter
from typing import Optional
from copy import deepcopy

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = [
    '$ cd /',
    '$ ls',
    'dir a',
    '14848514 b.txt',
    '8504156 c.dat',
    'dir d',
    '$ cd a',
    '$ ls',
    'dir e',
    '29116 f',
    '2557 g',
    '62596 h.lst',
    '$ cd e',
    '$ ls',
    '584 i',
    '$ cd ..',
    '$ cd ..',
    '$ cd d',
    '$ ls',
    '4060174 j',
    '8033020 d.log',
    '5626152 d.ext',
    '7214296 k'
]


class Dir:
    def __init__(self, name, parent: Dir = None):
        self.name: str = name
        self.files: dict[str] = {}
        self.dirs: list[Dir] = []
        self.parent: Optional[Dir] = parent
        self.size: int = 0

    def __repr__(self):
        return self.name


def get_commands(data: list[str]):
    commands = []
    outputs = []
    for i, _cmd in enumerate(data):
        if _cmd == '$ cd /':
            continue
        cmd = _cmd.split(' ')
        if cmd[0] == '$':
            commands.append((i, cmd))
    for i, cmd in enumerate(commands):
        if cmd[1][1] == 'ls':
            prev_idx = cmd[0]
            try:
                next_idx = commands[i + 1][0]
            except IndexError:
                next_idx = len(data)
            outputs.append(data[prev_idx + 1:next_idx])
    return commands, outputs


def get_size(folder: Dir, sum: int = 0, threshold:int = 100000) -> int:
    if folder.size <= threshold:
        print(f'{folder.name}: {folder.size}')
        sum += folder.size
    if len(folder.dirs) > 0:
        for subdir in folder.dirs:
            sum = get_size(subdir, sum)
    return sum


def solve(data: list[str], result: int = 0, part1=True) -> int:
    root = Dir('root')
    cur_dir = root
    i_output = 0
    commands, output = get_commands(data)
    for _cmd in commands:
        cmd = _cmd[1]
        if cmd[1] == 'ls':
            for entry in output[i_output]:
                fields = entry.split(' ')
                if fields[0] == 'dir':
                    cur_dir.dirs.append(Dir(name=fields[1], parent=cur_dir))
                else:
                    cur_dir.files[fields[1]] = int(fields[0])
                    cur_dir.size += int(fields[0])
                    if cur_dir.parent is not None:
                        cur_dir.parent.size += int(fields[0])
            i_output += 1
        elif cmd[1] == 'cd':
            if cmd[2] == '..':
                cur_dir = cur_dir.parent
            else:
                for _dir in cur_dir.dirs:
                    if _dir.name == cmd[2]:
                        cur_dir = _dir
                        break
    result = get_size(root)
    return result


timing_1 = perf_counter()
answer_1 = solve(test)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")

