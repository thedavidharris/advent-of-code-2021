#!/usr/bin/env python3
from pprint import pprint
from collections import Counter, defaultdict
import re

input = [[int(x) for x in line.replace(" -> ", ",").split(",")] for line in open("input.txt").read().splitlines()]

points = Counter()

for line in input:
    x1,y1,x2,y2 = line
    if (x1 == x2):
        y1, y2 = min(y1, y2), max(y1, y2)
        for y in range(y1, y2+1):
            points[(x1, y)] += 1
    elif (y1 == y2):
        x1, x2 = min(x1, x2), max(x1, x2)
        for x in range(x1, x2+1):
            points[(x, y1)] += 1

print(sum(x > 1 for x in points.values()))


