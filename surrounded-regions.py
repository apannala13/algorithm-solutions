from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])
        visit = set()

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visit.add((r, c))
            component = []
            component.append((r, c))
            is_boundary_connected = r == 0 or c == 0 or r == rows - 1 or c == cols - 1 #flag which becomes True if any cells are on boundary
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            while queue:
                nr, nc = queue.popleft()
                for dr, dc in directions:
                    rr, cc = nr + dr, nc + dc
                    if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc] == 'O' and ((rr, cc)) not in visit:
                        visit.add((rr, cc))
                        queue.append((rr, cc))
                        component.append((rr, cc))
                        if rr == 0 or cc == 0 or rr == rows - 1 or cc == cols - 1:
                            is_boundary_connected = True

            if not is_boundary_connected:
                for row, col in component:
                    board[row][col] = 'X'

        for r in range(rows):
            for c in [0, cols-1]:
                if board[r][c] == 'O' and (r, c) not in visit:
                    bfs(r, c)
        for c in range(cols):
            for r in [0, rows-1]:
                if board[r][c] == 'O' and (r, c) not in visit:
                    bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visit:
                    board[r][c] = 'X'




if __name__ == "__main__":
  pass
  
