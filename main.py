#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import argparse
import random
import copy
import os


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
    for strin in maps:
        for el in strin:
            print(el, end='', sep='')
        print()
    break
    os.system('cls' if os.name == 'nt' else 'clear')