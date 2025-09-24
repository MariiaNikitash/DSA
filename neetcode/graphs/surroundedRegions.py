'''
Surrounded Regions
Solved 
You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

Example 1:

Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]
Explanation: Note that regions that are on the border are not considered surrounded regions.

Constraints:

1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.

Time: O(n*m)
Space: O(n*m)

I'm so happy i solved it :)
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

    
    # DFS only runs on the border cells
        def capture(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c-1)
            capture(r, c+1)
    # 1. DFS Capture unsurrounded regions and convert to O -> T
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    capture(r,c)

    # 2. Capture surrounded regions (O->X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
    # 3. Uncapture unsurrounded regions (T->O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
     