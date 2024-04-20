class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return None
        
        board = heights #reference -> heights. like board better.
        rows, cols = len(board), len(board[0]) 
        pacific_queue, atlantic_queue = deque(), deque()
        pacific_set, atlantic_set = set(), set() #track visited cells for both oceans

        for r in range(rows):
            pacific_queue.append((r, 0)) #every row, first col -> left side for pacific
            atlantic_queue.append((r, cols - 1)) #every row, last col -> right side for atl
            pacific_set.add((r, 0))
            atlantic_set.add((r, cols - 1))
        
        for c in range(cols):
            pacific_queue.append((0, c)) #first row, every column -> pacific top bound 
            atlantic_queue.append((rows - 1, c)) #last row, every col -> atl bottom bound
            pacific_set.add((0, c))
            atlantic_set.add((rows - 1, c))
        def bfs(queue, visit):
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc 
                    #check if the neighboring cell (nr, nc) has a higher or equal elevation
                    #compared to current cell (cr, cc). Ensures that water can 
                    #potentially flow from the neighboring cell to the current cell,
                    #since water flows downhill or remains level.
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] >= board[cr][cc] and ((nr, nc)) not in visit:
                        queue.append((nr, nc))
                        visit.add((nr, nc))
        
        bfs(pacific_queue, pacific_set)
        bfs(atlantic_queue, atlantic_set)

        #collect all cells that can reach both Pacific and Atl oceans, set intersection
        res = [list(cell) for cell in pacific_set & atlantic_set]
        return list(res) 
