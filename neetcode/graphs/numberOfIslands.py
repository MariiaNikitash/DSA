from collections import deque

def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0 

    def bfs(r,c):
        q = deque()
        visited.add((r,c))
        q.append((r,c))
        while q:
            row,col = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0, -1]]

            for dr, dc in directions:
                # chek if in bounds
                new_r, new_c = row + dr, col + dc
                if (new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == '1' and (new_r,new_c) not in visited):
                    visited.add((new_r,new_c))
                    q.append((new_r,new_c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                bfs(r,c)
                islands += 1
    

    return islands


grid1 = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
#Output: 1

grid2 = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
#Output: 4 

print(numIslands(grid1))