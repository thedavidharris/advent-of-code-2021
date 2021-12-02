#!/usr/bin/env python3

with open("input.txt") as f:
    input = [int(x) for x in f.read().splitlines()]

print(sum(b > a for a, b in zip(input, input[1:])))
