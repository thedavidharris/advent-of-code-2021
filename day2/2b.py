#!/usr/bin/env python3

horizontal=depth=aim=0

for line in open("input.txt"):
    dir,mag = line.split()
    if dir == 'forward':
        horizontal += int(mag)
        depth += aim*int(mag)
    if dir == 'down':
        aim += int(mag)
    if dir == 'up':
        aim -= int(mag)

print(horizontal*depth)


