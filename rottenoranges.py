class Oranges:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
            
      # Find all initially rotten oranges and start the BFS from each of them
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))   # Append coordinates and minute (time)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minutes = 0 
        
        while queue:
            r, c, minute = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2 #mark as rotten
                    queue.append((nr, nc, minute + 1))
                    minutes = max(minutes, minute + 1)
                  
        # If any fresh oranges left, return -1
        for row in grid:
            if 1 in row:
                return -1
        return minutes 
if __name__ == "__main__":
  o = Oranges()
  pass  #add testcases 
