from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN

import pandas as pd

import common

lines = common.read_input_lines_to_list(2021, 4)

selections = lines[0]

boards = {}
board = []
board_id = 0
for line in lines[1:]:
    if board and line == '':
        boards[board_id] = board
        board_id += 1
        board = []
    elif line != '':
        row = [{int(n): False} for n in line.split(' ') if len(n) > 0]
        # row = [int(n) for n in line.split(' ') if len(n) > 0]
        board.append(row)


def select_number(n, boards):
    for k, board in boards.items():
        for row in board:
            for cell in row:
                if n in cell.keys():
                    cell[n] = True

    return boards


def check_row(row):
    for cell in row:
        for k, v in cell.items():
            if not v:
                return False
    return True

def check_board(board):
    for row in board:
        if check_row(row):
            return True

    cols = [[board[i][j]for i in range(5)]for j in range(5)]
    for col in cols:
        if check_row(col):
            return True
    return False


def sum_of_unmarked(board):
    s = 0
    for row in board:
        for col in row:
            for k, v in col.items():
                if not v:
                    s += k
    return s


def play_round(boards, selection):
    boards = select_number(int(selection), boards)
    to_remove = []
    for board_id, board in boards.items():
        if check_board(board):
            print(f'board: {board_id} has a bingo with selection: {selection}')
            for row in board:
                print(row)
            s = sum_of_unmarked(board)
            print(f'sum = : {s}, last_number = {selection}')
            print(f'score = {s * int(selection)}')
            to_remove.append(board_id)
            # return True

    if len(boards) == 1 and len(to_remove) > 0:
        for board_id, board in boards.items():
            for row in board:
                print(row)
            s = sum_of_unmarked(board)
            print(f'sum = : {s}, last_number = {selection}')
            print(f'score = {s * int(selection)}')
    for i in to_remove:
        boards.pop(i, None)

# looking back i wouldve done this very differently but the brute force method worked fairly well



# for selection in selections.split(','):
#     if play_round(boards, selection):
#         break

for selection in selections.split(','):
    play_round(boards, selection)
    if len(boards) == 0:
        break

print(boards)

# boards = select_number(59, boards)
# print(check_board(boards[0]))
# boards = select_number(98, boards)
#
# print(check_board(boards[0]))
# boards = select_number(84, boards)
# boards = select_number(27, boards)
# boards = select_number(56, boards)
# print(boards[0])
# print(check_board(boards[0]))
# [[59, 98, 84, 27, 56], [17, 35, 18, 64, 34], [62, 16, 74, 26, 55], [21, 99, 1, 19, 93], [65, 68, 53, 24, 73]]