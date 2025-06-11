import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def init_board():
    board = [[0]*4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty:
        return
    i, j = random.choice(empty)
    board[i][j] = 4 if random.random() < 0.1 else 2

def print_board(board):
    clear()
    print("---- 2048 Game ----\nUse W A S D to move. Q to quit.\n")
    for row in board:
        print("+------+------+------+------+") 
        print("|" + "|".join(f"{num:^6}" if num > 0 else "      " for num in row) + "|")
    print("+------+------+------+------+")

def compress(row):
    new_row = [num for num in row if num != 0]
    for i in range(len(new_row)-1):
        if new_row[i] == new_row[i+1]:
            new_row[i] *= 2
            new_row[i+1] = 0
    new_row = [num for num in new_row if num != 0]
    return new_row + [0]*(4 - len(new_row))

def move_left(board):
    return [compress(row) for row in board]

def move_right(board):
    return [compress(row[::-1])[::-1] for row in board]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_up(board):
    transposed = transpose(board)
    moved = move_left(transposed)
    return transpose(moved)

def move_down(board):
    transposed = transpose(board)
    moved = move_right(transposed)
    return transpose(moved)

def has_moves(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return True
            if i < 3 and board[i][j] == board[i+1][j]:
                return True
            if j < 3 and board[i][j] == board[i][j+1]:
                return True
    return False

def main():
    board = init_board()
    while True:
        print_board(board)
        move = input("Your move (WASD/Q): ").lower()
        if move == 'q':
            print("Bye!")
            break
        elif move in ['w', 'a', 's', 'd']:
            if move == 'w':
                new_board = move_up(board)
            elif move == 's':
                new_board = move_down(board)
            elif move == 'a':
                new_board = move_left(board)
            else:
                new_board = move_right(board)
            if new_board != board:
                board = new_board
                add_new_tile(board)
            if not has_moves(board):
                print_board(board)
                print("Game Over!")
                break
        else:
            print("Invalid input. Please use W, A, S, D or Q.")

if __name__ == "__main__":
    main()
