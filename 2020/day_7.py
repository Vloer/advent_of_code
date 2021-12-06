from typing import List, Dict, Union
import os
import re

'''
Sample input:
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

x y bags contain n x y bag(s), n x y bag(s), n x y bag(s). ...

Elke soort bag moet een key zijn met als values de bags die ze hebben + de hoeveelheid
'''

ROOT = "C:\\Users\\RuweBo01\\Anaconda3\\Scripts\\Advent of code"
input_filee = "7_input_test.txt"
input_file = os.path.join(ROOT, input_filee)


def parse_input(txt_file: str = input_file) -> List[str]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


def extract_data(s: str) -> Dict[str, List[str]]:
    '''
    Sample input:
    light red bags contain 1 bright white bag, 2 muted yellow bags.

    Sample output:
    {
        'light red': 
        {
            'bright white': 1,
            'muted yellow': 2
        }
    }
    '''
    out = {}
    if "no other bags" in s:
        bag = ' '.join(s.split()[:2])
        out[bag] = []
    else:
        reg_whole_sentence = re.compile(r"(\w+ \w+) bags contain (((\d+ \w+ \w+ \w+),?\.? ?)+)")
        att_list = list(reg_whole_sentence.findall(s)[0])
        parent_bag = att_list[0] # light red
        key_children = att_list[1] # 1 bright white bag, 2 muted yellow bags.
        reg_child_bags = re.compile(r"((\d+) (\w+ \w+) \w+)+")
        child_bags = list(reg_child_bags.findall(key_children))

        out[parent_bag] = []

        for bag in child_bags:
            bag_color = bag[2]
            bag_amount = bag[1]
            out[parent_bag].append(bag_color)

    return out

def extract_data_all(input: List) -> Dict[str, List[str]]:
    out = {}
    for rule in input: 
        new_data = extract_data(rule)
        out.update(new_data)

    return out

all = extract_data_all(parse_input())
good = []
for k, v in all.items():
    if "shiny gold" in v:
        ggggggggggggggggggggggggg35cv xxxxxxx56

print("List of bags with gold: " + good)

