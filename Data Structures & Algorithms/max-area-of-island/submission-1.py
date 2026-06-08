class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]    
        rows, cols = len(grid), len(grid[0])
        visited = set()
        self.res = 0
        self.cur = 0

        def dfs(i, j):
            if i<0 or j<0 or i>=rows or j>=cols or (i,j) in visited or grid[i][j]==0:
                return

            visited.add((i,j))
            self.cur += 1
            self.res = max(self.res, self.cur)

            for di, dj in dirs:
                dfs(i+di, j+dj)                

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]==1:
                    self.cur = 0
                    dfs(r, c)

        return self.res            
        