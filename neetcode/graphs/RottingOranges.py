#Rotting Orranges
# Multisource BFS 
# keep track of how many rotten oranges and how many fresh oranges ititially
# then add roten to a q and roess them while decrementing fresh oranges when nei is rotten
# after q iteration is over increment minutes
# return minutes if all fruits became rotten else -1
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                # count fresh of == 1
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [(-1,0), (1,0), (0,-1), (0, 1)]        
       # 
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r < 0 or new_r == rows or new_c < 0 or new_c == cols or grid[new_r][new_c] != 1):
                        continue
                    fresh -=1
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))
            minutes += 1

        return minutes if fresh == 0 else -1
        # 

        # we iterate over grid[r][c] to count all fresh oranges
        # and add all rotten to a que then we update the q performing bfs
        # and adding more rotten fruits 
        # if grid[r][c] == 2 : we perform bfs and mark its
        # neighbors as 2  

        # return min number of minutes else -1

        #Time: O(m × n)
        #Space: O(m × n)