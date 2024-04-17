from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None
            
        rows, cols = len(board), len(board[0])
        visit = set()
        def bfs(r, c):
            queue = deque()
            component = [(r, c)]  #holds all the cells of a connected group of 'O's that are reached during the BFS from a starting cell. Initialize it with current cell
            queue.append((r, c))
            visit.add((r, c))  # Mark starting cell as visited

            # flag to check if cell is within the boundary of grid
            is_boundary = r == 0 or c == 0 or r == rows - 1 or c == cols - 1
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            while queue:
                qr, qc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr, nc) not in visit:
                        # mark neighbor as visited and add to the queue and component list
                        visit.add((nr, nc))
                        queue.append((nr, nc))
                        component.append((nr, nc))
                        # upd boundary status if the neighbor is on the boundary
                        if nr == 0 or nc == 0 or nr == rows - 1 or nc == cols - 1:
                            is_boundary = True
            
            #if the component is not connected to any boundary, mark all its cells as 'X'.
            if not is_boundary:
                for row, col in component:
                    board[row][col] = "X"

        # start BFS from all 'O's on the vertical border
        for r in range(rows):
            for c in [0, cols-1]:
                if board[r][c] == "O" and (r, c) not in visit:
                    bfs(r, c)

        # start BFS from all 'O's on the horizontal border
        for c in range(cols):
            for r in [0, rows-1]:
                if board[r][c] == "O" and (r, c) not in visit:
                    bfs(r, c)

        # mark all other unvisited 'O's to 'X'.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"
