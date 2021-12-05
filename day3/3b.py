#!/usr/bin/env python3

input = [[int(i) for i in x.strip()] for x in open("input.txt")]

def lsr(inp, out_num):
    col = 0
    while len(inp) > 1:
        column = list(zip(*inp))[col]
        if sum(column) / len(column) >= 0.5:
            b = out_num
        else:
            b = (out_num + 1) % 2
        inp = [x for x in inp if x[col] == b]
        col += 1
    return "".join(str(x) for x in inp[0])

oxygen = lsr(input, 1)
co2 = lsr(input, 0)
print(int(oxygen, 2) * int(co2, 2))


