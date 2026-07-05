class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def dfs(i, j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for di, dj in directions:
                if 0<=i+di<rows and 0<=j+dj<cols and grid[i+di][j+dj]=='1':
                    dfs(i+di, j+dj)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    islands += 1
                    dfs(i,j)
        return islands            
        