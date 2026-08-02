class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        visited = set()

        def dfs(i, j):
            visited.add((i,j))
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]=='1' and (ni,nj) not in visited:
                    dfs(ni, nj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    islands += 1
                    dfs(i,j)
        
        return islands            
        