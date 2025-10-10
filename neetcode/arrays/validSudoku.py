'''
Valid Sudoku
Solved 
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

time and space is N^2'''
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in row_set[r] or 
                    board[r][c] in col_set[c] or
                    board[r][c] in squares[(r // 3 , c // 3)]):
                    return False
                
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True


