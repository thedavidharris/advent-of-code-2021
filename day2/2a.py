#!/usr/bin/env python3

h=0
d=0

for line in open("input.txt"):
    dir,mag = line.split()
    if dir == 'forward':
        h += int(mag)
    if dir == 'down':
        d += int(mag)
    if dir == 'up':
        d -= int(mag) 

print(h*d)


