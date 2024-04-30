class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        grid = image 
        
        if grid[sr][sc] == color:
            return grid  #sr, sc is starting point. if its already target color then avoid unecessayr processing.

        rows, cols = len(grid), len(grid[0])
        
        queue = collections.deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        original_color = grid[sr][sc] #original color of the starting cell
        
        def bfs(sr, sc):
            queue.append((sr, sc)) 
            while queue:
                r, c = queue.popleft()
                if grid[r][c] == original_color: #if cell is not target color,
                    grid[r][c] = color  #fill cell with color
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc  #new cell's coordinates
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == original_color: #add new cell to queue if it has the original color
                            queue.append((nr, nc))
                        
                            
        bfs(sr, sc)
        return grid 
    
                    
        
