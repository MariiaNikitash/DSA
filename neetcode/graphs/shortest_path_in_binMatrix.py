from collections import deque
# When i think of shortest path -> BFS or ... Djistra
# get the path by counting 0s to get to the righ bottom most 0
def shortestPathBinMatrix(grid): 
    N = len(grid)
    if grid[0][0] == 1 or grid[N-1][N-1] == 1:
        return -1
    q = deque([(0,0,1)]) # r, c, length
    visited = {(0,0)}
    directions = [[0,1],[1,0],[0,-1],[-1,0],
                  [1,1],[-1,1],[-1,-1],[1,-1]]
    while q:
        r,c,length = q.popleft()
        if (r, c) == (N-1, N-1):
            return length
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, length + 1))
    return length
    

grid1 = [ [0,1],
          [1,0]]

# Output : 2 # diagonally to reach right bottom most val we need to have  2 nodes 
print(shortestPathBinMatrix(grid1))