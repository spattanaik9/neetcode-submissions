class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                
                for di, dj in dirs:
                    nr, nc = r+di, c+dj
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]!=-1 and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))

            dist += 1        
        