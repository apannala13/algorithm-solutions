

"""
leetcode bfs traversal solution for finding max number of islands (marked with '1' in a grid)

"""
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 #edge case for empty grid

        visit = set()  #kepp track of visited cells
        rows, cols = len(grid), len(grid[0])  #dimensions for rows and cols
        islands = 0 #counter for number of islands

        def bfs(r, c):
            queue = collections.deque()
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]] #possible directions to move
            queue.append((r, c)) #start bfs from current cell
            visit.add((r, c)) #mark current cell as visited
            while queue:
                cr, cc = queue.popleft() #deque front cell
                for dr, dc in directions: #explore each direction
                    nr, nc = cr + dr, cc + dc  #calculate new cell's coordinates
                    #check if new cell is inbounds, hasnt been visited and is an is land
                    if(0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit) and grid[nr][nc] == "1":
                        queue.append((nr, nc)) #add cell to queue
                        visit.add((nr, nc)) #mark cell as visited
            
        for r in range(rows):
            for c in range(cols):
                #check each cell if it's land and not visited to start bfs traversal
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c) #call bfs to explore island
                    islands += 1 
        return islands 

if __name__ == "__main__":
    pass #add testcases later
