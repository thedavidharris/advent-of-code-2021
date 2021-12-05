#!/usr/bin/env python3

columns = list(zip(*[[int(i) for i in x.strip()] for x in open("input.txt")]))

gamma = ''
epsilon = ''

for column in columns:
    if sum(column) / len(column) > 0.5:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)