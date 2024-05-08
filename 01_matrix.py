class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0: #mark all zeroes as visited
                    queue.append((r, c))
                    visit.add((r, c))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        #bfs to find shortest distance
        while queue:
            qr, qc = queue.popleft()
            for dr, dc in directions:
                nr, nc = qr + dr, qc + dc 
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    #update distance for each cell based on its nearest zero
                    mat[nr][nc] = mat[qr][qc] + 1
                    queue.append((nr, nc))
                    visit.add((nr, nc))

        return mat
