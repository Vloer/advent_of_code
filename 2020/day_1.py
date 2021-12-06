#!python3

import csv
import os

with open('1_input.txt', newline = '\n') as csvfile:
    l = csv.reader(csvfile)
    lijst = [] 
    for row in l:
        lijst.append(', '.join(row))

lijst = list(map(int, lijst))
# print(lijst)
tar = 2020

def test(il):
    for i in range(len(il)-1):
        for j in range(i, len(il)):
            for k in range(j, len(il)):
                out = il[i] + il[j] + il[k]
                if out == tar:
                    answer = il[i]*il[j]*il[k]
                    print(f"Found: {il[i]} times {il[j]} times {il[k]} is {answer}")
                    return(answer)
                

test(lijst)