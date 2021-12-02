from typing import List
import os

ROOT = "C:\\Users\\RuweBo01\\repos\\aoc\\inputs"
input_filee = "d2.txt"
input_file = os.path.join(ROOT, input_filee)


def parse_input(txt_file: str = input_file) -> List[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))

inp = parse_input()

def solve1() -> None:
  result = 0
  x = 0
  y = 0
  for i in inp:
    direction, num = i.split(" ")
    if "forward" in direction:
      x += int(num)
    if "down" in direction:
      y += int(num)
    if "up" in direction:
      y -= int(num)
  result = x*y
  print(result)

def solve2() -> None:
  result = 0
  x = 0
  y = 0
  aim = 0
  for i in inp:
    direction, num = i.split(" ")
    if "forward" in direction:
      x += int(num)
      y += aim * int(num)
    if "down" in direction:
      aim += int(num)
    if "up" in direction:
      aim -= int(num)
  result = x*y
  print(result)
      

solve1()
solve2()