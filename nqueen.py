#!/usr/bin/env python
# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017
# Updated by Mahesh Belnekar, 2018

import sys

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] )

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] )

# Count # of pieces in given diagonal
# 
# Logic to find points that lie on the diagonal:
# Every diagonal in the martrix can either have slope 1 or -1
# Thus, using the slope point form, we can find that,
# Point lying on the same diagonal have equal sum and difference between
# their row and column position
def count_on_diag(board, row, col):
    posDiff = row-col
    posAdd = row + col
    summation = 0
    for r in range(0, N):
        for c in range(0,N):
            if r-c == posDiff or r+c == posAdd:
                summation += board[r][c]
    return summation

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# For printing we need to get the character to print
# For queens its "Q" and "R" for rooks
def getPrintChar(board, r, c):
    if notAvailableBoard[r][c] != 0:
        return "X"

    if board[r][c] != 0:
        return PrintSymbol

    return "_"

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ " ".join([ getPrintChar(board, r, c) for c in range(0, N) ]) for r in range(0, N)])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
# But eliminate the successors which have more than N rooks or
# which do not add any new rooks
# only allowed to add a piece to the leftmost column of the board that is currently empty.
def successors(board):
    returnArray = []
    # If we already have N pieces on our board, we cannot keep adding further
    # Add only if there are less than N pieces on the board
    if(count_pieces(board) < N):

        # Find the leftmost free column
        column = 0
        for c in range(0,N):
            if count_on_col(board, c) == 0:
                column = c
                break

        for r in range(0,N):
            if count_on_row(board, r) != 0:
                continue
            # First check if this position is available or not
            if notAvailableBoard[r][column] != 0:

                continue
            if PrintSymbol == 'Q' and count_on_diag(board, r, column) != 0:
                continue

            returnArray.append(add_piece(board, r ,column))

    return returnArray

# check if board is a goal state
def is_goal(board):

    if count_pieces(board) != N:
        return False


    for r in range(0, N):
        if count_on_row(board, r) > 1:
            return False

    for c in range(0, N):
        if count_on_col(board, c) > 1:
            return False

    for r in range(0, N):
        for c in range(0, N):
            if board[r][c] != 1:
                continue
            if PrintSymbol == 'Q' and count_on_diag(board, r, c) > 1:
                return False
    return True

# Solve
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors( fringe.pop() ):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False

# PrintSymbol signifies the type of problem, 'nrook' or 'nqueen'
PrintSymbol = "Q" if sys.argv[1] == "nqueen" else "R"

# This is N, the size of the board. It is passed through command line arguments.
N = int(sys.argv[2])

NumberOfUnavailablePositions = int(sys.argv[3])

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N for i in range(N)]

# This board indicates which squares are not notAvailable
# 0 indicates available, 2 indicates not available
notAvailableBoard = [[0]*N for i in range(N)]

offSet = 4
for k in range (0, NumberOfUnavailablePositions):
    notAvailableBoard[int(sys.argv[offSet])-1][int(sys.argv[offSet+1])-1] = 2
    offSet = offSet + 2

solution = solve(initial_board)
print (printable_board(solution) if solution else "Sorry, no solution found. :(")
