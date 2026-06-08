class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(i, j):
            if (i<0 or i>=rows or j<0 or j>=cols or grid[i][j]=='0' or (i,j) in visited):
                return
            visited.add((i,j))

            for di, dj in dirs:
                dfs(i+di, j+dj)    

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == '1':
                    res += 1
                    dfs(r,c)

        return res               
        