# Multisource BFS problem, where we update distance in all neighbors at a time

# LC: Walls and Gates (Islands and Treasures)
'''
You are given a
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
'''
from collections import deque
class Solution:
    def islandsAndTreasure(grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        

        def addCell(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or
                (r, c) in visited or grid[r][c] == -1
            ):
                return
            visited.add((r, c))
            q.append([r, c])
            



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1


            
