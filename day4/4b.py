#!/usr/bin/env python3
from pprint import pprint

with open("input.txt") as f:
    input = f.read().split("\n\n")

draws = input[0].split(",")
boards = [[x.split() for x in x.strip().split("\n")] for x in input[1:]]

def check_board(draws, board):
    for i in range(5):
        if all(board[i][j] in draws for j in range(5)) or all(board[j][i] in draws for j in range(5)):
            return True
    return False

winners = [False for _ in range(len(boards))]

for i in range(1, len(draws)):
    current_draws = list(dict.fromkeys(draws[:i]))
    for j, board in enumerate(boards):
        if check_board(current_draws, board):
            winners[j] = True

            if all(winners):
                winning_board = board
                winning_draws = current_draws

                unmarked = 0
                for i in range(5):
                    for j in range(5):
                        if winning_board[i][j] not in winning_draws:
                            unmarked += int(winning_board[i][j])
                print(unmarked * int(winning_draws[-1]))
                exit()
