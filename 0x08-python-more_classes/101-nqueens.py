#!/usr/bin/python3
"""Wahala"""
import sys


def is_valid(columns, row, col):
    for r in range(row):
        c = columns[r]
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def solve_n_queens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    columns = [-1] * n
    solutions = []
    
    def backtrack(row):
        if row == n:
            solutions.append([ [i, columns[i]] for i in range(n)])
            return
        for col in range(n):
            if is_valid(columns, row, col):
                columns[row] = col
                backtrack(row + 1)
                columns[row] = -1
    
    backtrack(0)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    solve_n_queens(N)

