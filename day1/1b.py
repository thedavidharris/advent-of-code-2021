#!/usr/bin/env python3

with open("input.txt") as f:
    input = [int(x) for x in f.read().splitlines()]

groups = [sum(x) for x in zip(input, input[1:], input[2:])]
print(sum(b > a for a, b in zip(groups, groups[1:])))
