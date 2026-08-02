class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def dfs(r, c):
            visited.add((r,c))
            cur = 1
            for dr, dc in directions:
                nr, nc = r+dr, c + dc
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == 1:
                    cur += dfs(nr, nc)

            return cur
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    islands = max(islands, dfs(i,j))

        return islands            
        