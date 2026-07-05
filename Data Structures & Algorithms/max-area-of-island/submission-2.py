class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()

        def dfs(i, j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            self.cur += 1
            for di, dj in directions:
                if 0<= i+di < rows and 0 <= j + dj < cols and (i+di, j+dj) not in visited and grid[i+di][j+dj] == 1:
                    dfs(i+di, j+dj)

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    self.cur = 0
                    dfs(i, j)
                    res = max(res, self.cur)
        return res            

        