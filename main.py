import copy
import os
import random
import time


def is_valid(board, row, col, num):
    # check is num legal in row
    if num in board[row]:
        return False

    # check is num legal in col
    for i in range(9):
        if num == board[i][col]:
            return False

    # check is num legal in 3*3 matrix
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if num == board[r][c]:
                return False

    return True


def fill_board(board, row=0, col=0):
    if row == 9:
        return True

    if col < 8:
        next_row, next_col = row, col + 1
    else:
        next_row, next_col = row + 1, 0

    if board[row][col] != 0:
        return fill_board(board, next_row, next_col)

    for num in random.sample(range(1, 10), 9):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if fill_board(board, next_row, next_col):
                return True
            board[row][col] = 0

    return False


def check_remove(board, row=0, col=0, counter=None):

    if counter is None:
        counter = [0]

    if row == 9:
        counter[0] += 1
        return

    # end recursion if not only one solution
    if counter[0] > 1:
        return True

    if col < 8:
        next_row, next_col = row, col + 1
    else:
        next_row, next_col = row + 1, 0

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            check_remove(board, next_row, next_col, counter)
            board[row][col] = 0

    return False


def remove_num(board, count):
    board_copy = copy.deepcopy(board)

    current_count = 0

    while current_count < count:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board_copy[row][col] == 0:  # 確保選擇一個非零元素
            row = random.randint(0, 8)
            col = random.randint(0, 8)

        counter = [0]

        remove_num = board_copy[row][col]
        board_copy[row][col] = 0

        check_remove(board_copy, counter=counter)
        if counter[0] > 1:
            board_copy[row][col] = remove_num
        else:
            current_count += 1

    return board_copy

def solve(board, row=0, col=0, start_line=0):

    if row == 9:
        return True

    if col < 8:
        next_row, next_col = row, col + 1
    else:
        next_row, next_col = row + 1, 0

    if board[row][col] != 0:
        return solve(board, next_row, next_col, start_line)


    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            print_board(board, start_line)
            if solve(board, next_row, next_col, start_line):
                return True
            else:
                board[row][col] = 0

    return False


def print_board(board, start_line):
    # local the start line
    print(f"\033[{start_line}H", end="")

    # clear content form the start line to end
    print("\033[J", end="")

    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

    time.sleep(0.01)

if __name__ == '__main__':

    os.system('cls')  # 清空命令行窗口

    # define a 9*9 matrix
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    new_board = remove_num(board, 35)

    for row in new_board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

    print("\n-------------------------------\n")

    start_line = 13
    solve(new_board, start_line=start_line)