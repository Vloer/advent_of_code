from __future__ import annotations
from pathlib import Path
from time import perf_counter
from typing import Optional
from copy import deepcopy
from collections import defaultdict

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


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = []

    def __repr__(self):
        return f'Dir {self.name} {self.size}'

    def get_dir(self, name):
        for d in self.dirs:
            if d.name == name:
                return d
        return None

    def add_dir(self, dir):
        if dir.name not in [d.name for d in self.dirs]:
            self.dirs.append(dir)

    def add_file(self, file):
        if file.name not in [f.name for f in self.files]:
            self.files.append(file)

    @property
    def size(self):
        return sum([d.size for d in self.dirs]) + self.size_files

    @property
    def size_files(self):
        return sum([f.size for f in self.files])


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'File {self.name} {self.size}'


def collect_directories(directory_obj):
    directories = []
    for dir_obj in directory_obj.dirs:
        directories.append(dir_obj)
        directories.extend(collect_directories(dir_obj))
    return directories


def build_data(data: list[str]) -> Dir:
    commands, outputs = get_commands(data)
    root = Dir('/')
    current_dir = root
    outputs_parsed = 0
    for i, cmd in enumerate(commands):
        if cmd[1][1] == 'ls':
            for x in outputs[outputs_parsed]:
                if x.startswith('dir'):
                    dirname = x.split(' ')[1]
                    current_dir.add_dir(Dir(dirname, parent=current_dir))
                else:
                    size, name = x.split(' ')
                    f = File(name, int(size))
                    current_dir.add_file(f)
            outputs_parsed += 1
        elif cmd[1][1] == 'cd':
            target_dir = cmd[1][2]
            if target_dir == '..':
                target = current_dir.parent
            else:
                target = current_dir.get_dir(target_dir)
            current_dir = target
    return root


def solve(data: list[str], result: int = 0, part1=True):
    system = build_data(data)
    dirs = collect_directories(system)
    if part1:
        return sum([d.size for d in dirs if d.size <= 100_000])
    max_size = 70_000_000
    needed_size = 30_000_000
    unused = max_size - system.size
    required = needed_size - unused
    smallest = 99999999
    for d in dirs:
        if smallest > d.size >= required:
            smallest = d.size
    return smallest


timing_1 = perf_counter()
answer_1 = solve(test)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
