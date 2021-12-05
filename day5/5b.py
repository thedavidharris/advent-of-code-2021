#!/usr/bin/env python3
from collections import Counter

sign = lambda x: bool(x > 0) - bool(x < 0)

input = [[int(x) for x in line.replace(" -> ", ",").split(",")] for line in open("input.txt").read().splitlines()]

points = Counter()

for line in input:
    x1,y1,x2,y2 = line
    dx = sign(x2-x1)
    dy = sign(y2-y1)
    points[(x1,y1)] += 1
    while x1 != x2 or y1 != y2:
        x1 += dx
        y1 += dy
        points[(x1,y1)] += 1

print(sum(x > 1 for x in points.values()))


