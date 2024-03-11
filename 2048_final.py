# This is 2048 game, I think you have already played the game before in mobile, but if you haven't then you can search it on the playstore or appstore, it's pretty simple :)

import random
import copy

# This will print out the board in the way we want

def initializeBoard(boardSize):
    return [[0] * boardSize for _ in range(boardSize)]

def display(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else '.' for cell in row))
    print()

# This function picks a new value for the board and adds the value to the board
def addNewValue(board):
    emptyCells = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 0]
    if emptyCells:
        i, j = random.choice(emptyCells)
        board[i][j] = random.choice([2, 4])

def mergeRow(row):
    newRow = [0] * len(row)
    index = 0

    for value in row:
        if value != 0:
            if newRow[index] == 0:
                newRow[index] = value
            elif newRow[index] == value:
                newRow[index] *= 2
                index += 1
            else:
                index += 1
                newRow[index] = value
    return newRow

# This functions merge the row to left or right or up or down or to transpose
def mergeLeft(board):
    return [mergeRow(row) for row in board]

def mergeRight(board):
    reversed_rows = [row[::-1] for row in board]
    merged_rows = [mergeRow(row) for row in reversed_rows]
    return [row[::-1] for row in merged_rows]

def transpose(board):
    return [list(row) for row in zip(*board)]

def mergeUp(board):
    transposed_board = transpose(board)
    merged_board = mergeLeft(transposed_board)
    return transpose(merged_board)

def mergeDown(board):
    transposed_board = transpose(board)
    merged_board = mergeRight(transposed_board)
    return transpose(merged_board)

# This function tests if the user won
def gameOver(board):
    for row in board:
        if 2048 in row:
            return True

# This function tests if the user has lost
    tempboard1 = copy.deepcopy(board)
    tempboard2 = copy.deepcopy(board)

    tempboard1 = mergeDown(tempboard1)
    if tempboard1 == tempboard2:
        tempboard1 = mergeUp(tempboard1)
        if tempboard1 == tempboard2:
            tempboard1 = mergeLeft(tempboard1)
            if tempboard1 == tempboard2:
                tempboard1 = mergeRight(tempboard1)
                if tempboard1 == tempboard2:
                    return True
    return False

# Creating the board
def main():
    boardSize = 4
    board = initializeBoard(boardSize)
    addNewValue(board)
    addNewValue(board)

    # Figures out which way the person wants to merge and use the correct function
    while True:
        display(board)
        move = input("Enter your move (W/A/S/D): ").upper()

        if move == 'W':
            board = mergeUp(board)
        elif move == 'A':
            board = mergeLeft(board)
        elif move == 'S':
            board = mergeDown(board)
        elif move == 'D':
            board = mergeRight(board)
        elif move == 'Q':
            break
        else:
            print("Invalid move. Use W/A/S/D to move or Q to quit.")

        addNewValue(board)

        if gameOver(board):
            display(board)
            print("Game Over!")
            break

# checks if the script is being run as the main program
if __name__ == "__main__":
    main()
