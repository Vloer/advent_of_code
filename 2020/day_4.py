#!python3

from typing import List, Dict, Union
import os
import re

ROOT = "C:\\Users\\RuweBo01\\Anaconda3\\Scripts\\Advent of code"
input_filee = "4_input.txt"
input_file = os.path.join(ROOT, input_filee)

def parse_input(txt_file: str = input_file) -> List[str]:
    with open(txt_file, 'r') as f:
        inp = f.read().split("\n\n")
        inp = [x.replace("\n", " ") for x in inp]
        inpp = [[]]
        for i in range(len(inp)):
            inpp.append([])
            for j in inp[i].split(" "):
                inpp[i].append(j)
        return(inpp)

all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def fill_passport_list(passport_list: List) -> List[dict]:
    passports = []
    for i in range(len(passport_list)):
        passports.append({})
        for pw in passport_list[i]:
            k, v = pw.split(":")
            passports[i][k] = v
    return(passports)

def check_keys(passport_dict: Dict, required: List) -> bool:
    if all (k in passport_dict.keys() for k in required):
        return True
    else:
        return False

def check_validity(k: str, v: Union[str, int]) -> bool:
    if k == "byr":
        return(1920 <= int(v) <= 2002)
    elif k == "iyr": 
        return(2010 <= int(v) <= 2020)
    elif k ==  "eyr": 
        return(2020 <= int(v) <= 2030)
    elif k == "hgt": 
        pat = re.compile("^([0-9]+)([a-z]+)$")
        res = pat.findall(v)
        if len(res) > 0:
            result = list(pat.findall(v)[0])
            if result[1] == "in":
                return(59 <= int(result[0]) <= 76)
            elif result[1] == "cm":
                return(150 <= int(result[0]) <= 193)
            else:
                return False
        else:
            return False
    elif k == "hcl": 
        return(bool(re.match("^#[A-Za-z0-9]{6}$", str(v))))
    elif k == "ecl": 
        return(v in ["amb", "blu", "brn", "grn", "gry", "grn", "hzl", "oth"])
    elif k == "pid": 
        return(bool(re.match("^[0-9]{9}$", str(v))))
    elif k == "cid":
        return True

def check_all_keys_validity(passport_dict: Dict, result: bool = False) -> bool:
    for k in passport_dict.keys():
        global global_counter
        result = check_validity(k, passport_dict[k])
        if not result:
            print(f"{k} in passport {global_counter} is not valid: {passport_dict[k]}")
            break
    return(result)

def assignment_1():
    valid = 0
    all_passports = fill_passport_list(parse_input())
    for passport in all_passports:
        if check_keys(passport, required_keys):
            valid += 1
    print(f"Found [{valid}/{len(all_passports)}] valid passports in assignment 1")
    return(valid)

def assignment_2():
    valid = 0
    global global_counter
    global_counter = 0
    all_passports = fill_passport_list(parse_input())
    for passport in all_passports:
        global_counter += 1
        if check_keys(passport, required_keys) and check_all_keys_validity(passport):
            valid += 1
    print(f"Found [{valid}/{len(all_passports)}] valid passports in assignment 2")
    return(valid)


assignment_1()
assignment_2()

