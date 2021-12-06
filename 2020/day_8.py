#!python3

from typing import List
import os
import operator
from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap

ROOT = "C:\\Users\\RuweBo01\\Anaconda3\\Scripts\\Advent of code"
input_filee = "8_input.txt"
input_file = os.path.join(ROOT, input_filee)

def parse_input(txt_file: str = input_file) -> List[str]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


'''
acc +7 increases by "accumulator" by 7 and jumps to next command
jmp +2 executes the execution 2 lines below
nop does nothing
'''

op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}

commands_base = parse_input()
commands_check = [None] * len(commands_base)
nop_idx = [commands_base.index(i)
           for i in commands_base if i.startswith("nop")]
jmp_idx = [commands_base.index(i)
           for i in commands_base if i.startswith("jmp")]


def assignment_1(command_set):
    commands = command_set
    acc_cur = 0
    iter = 0

    while True:
        cmd = commands[iter]
        if commands_check[iter]:
            print(
                f"Command {commands[iter]} on line {iter+1} has already been executed once!")
            print(f"---Assignment 1: Accumulator size is {acc_cur}---")
            break
        commands_check[iter] = True
        opp = cmd[4]
        if cmd[:3] == "acc":
            acc_cur = op[opp](acc_cur, int(cmd[5:]))
        elif cmd[:3] == "jmp":
            iter = op[opp](iter, int(cmd[5:]))
            continue

        iter += 1


def assignment_2(command_set: List[str],
                 jmp_iter: int = 0,
                 nop_iter: int = 0,
                 ass_count: int = 0,
                 printing: bool = True):
    commands_check = [None] * len(commands_base)
    ass_count += 1
    commands = command_set
    acc_cur = 0
    iter = 0

    if printing:
        print("")

    while True:
        cmd = commands[iter]
        opp = cmd[4]

        if commands_check[iter]:
            if printing:
                print(f"Command '{cmd}' on line {iter+1} has already been executed once!")
                print(f"jmp [{jmp_iter}/{len(jmp_idx)-1}] nop [{nop_iter}/{len(nop_idx)-1}]")

            commands = commands_base[:]
            if jmp_iter == nop_iter:
                if jmp_iter <= len(jmp_idx)-1:
                    command_to_change = commands[jmp_idx[jmp_iter]]
                    command_new = "nop" + command_to_change[3:]
                    commands[jmp_idx[jmp_iter]] = command_new
                    if printing:
                        print(f"Changing '{command_to_change}' to '{command_new}' on idx {jmp_idx[jmp_iter]}")
                jmp_iter += 1
            elif jmp_iter > nop_iter:
                if nop_iter <= len(nop_idx)-1:
                    command_to_change = commands[nop_idx[nop_iter]]
                    command_new = "jmp" + command_to_change[3:]
                    commands[nop_idx[nop_iter]] = command_new
                    if printing:
                        print(f"Changing '{command_to_change}' to '{command_new}' on idx {nop_idx[nop_iter]}")
                nop_iter += 1
            elif jmp_iter >= len(jmp_idx)-1 and nop_iter >= len(nop_idx)-1:
                print(
                    f"All values changed on attempt {ass_count}. Operation failed")
                break
            if printing:
                print(f"---Attempt {ass_count} failed---")
            assignment_2(commands, jmp_iter, nop_iter, ass_count, printing)
            break

        commands_check[iter] = True

        if cmd[:3] == "acc":
            acc_cur = op[opp](acc_cur, int(cmd[5:]))
        elif cmd[:3] == "jmp":
            iter = op[opp](iter, int(cmd[5:]))
            continue

        if iter == len(command_set)-1:
            print(
                f"---Assignment 2: End reached on attempt {ass_count}. Final accumulator size: {acc_cur}---")
            break
        else:
            iter += 1

@timing
def run():
    assignment_1(commands_base)
    assignment_2(commands_base, printing = False)

run()