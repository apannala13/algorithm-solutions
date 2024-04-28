class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        #find all gates and add their positions to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: #0 = gate
                    queue.append((r, c))
        #BFS from each gate to find the minimum distance to all reachable rooms
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc #coordinates of neighboring cells
                #if not a wall and if an empty room (2147483647)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and grid[nr][nc] == 2147483647:
                    #upd. the adjacent cell with a value that is one greater than the current cell
                    grid[nr][nc] = grid[r][c] + 1 #update the distance of neighboring cell
                    queue.append((nr, nc)) #add the neighboring cell to continue BFS from there

        
