#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import argparse
import random
import copy
import os
import time

def neigboor_count(maps, strin, el, animal, height, width):
    fish_neighb = 0
    if el > 0 and maps[strin][el - 1] == animal:
        fish_neighb += 1
    if el + 1 < width and maps[strin][el + 1] == animal:
        fish_neighb += 1
    if strin + 1 < height and maps[strin + 1][el] == animal:
        fish_neighb += 1
    if strin > 0 and maps[strin - 1][el] == animal:
        fish_neighb += 1
    if strin > 0 and el > 0 and maps[strin - 1][el - 1] == animal:
        fish_neighb += 1
    if strin > 0 and el + 1 < width and maps[strin - 1][el + 1] == animal:
        fish_neighb += 1
    if el + 1 < width and strin + 1 < height and maps[strin + 1][el + 1] == animal:
        fish_neighb += 1
    if el > 0 and strin + 1 < height and maps[strin + 1][el - 1] == animal:
        fish_neighb += 1
    return fish_neighb

def change_el(maps, strin, el, height, width):
    if maps[strin][el] == '🗿':
        return '🗿'
    if maps[strin][el] == '🐠' or maps[strin][el] == '🦐':
        animal = maps[strin][el]
        fish_neighb = neigboor_count(maps, strin, el, animal, height, width)
        if fish_neighb < 2 or fish_neighb > 3:
            return '🌊'
        else:
            return animal
    else:
        fish_neighb = neigboor_count(maps, strin, el, '🐠', height, width)
        shrimp_neighb = neigboor_count(maps, strin, el, '🦐', height, width)
        if fish_neighb == 3:
            return '🐠'
        if shrimp_neighb == 3:
            return '🦐'
        return '🌊'



rand = ['🦐', '🐠', '🗿', '🌊']
parser = argparse.ArgumentParser(description='Height and width of ocean')
parser.add_argument('height', type=int)
parser.add_argument('width', type=int)
args = parser.parse_args()
height = args.height
width = args.width
maps = [None] * height
for i in range(height):
    maps[i] = [None] * width
for strin in range(height):
    for el in range(width):
        maps[strin][el] = random.choice(rand)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    for strin in range(height):
        for el in range(width):
            print(maps[strin][el], end='', sep='')
            maps[strin][el] = change_el(maps, strin, el, height, width)
        print()
    time.sleep(2)
