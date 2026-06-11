class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = collections.defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for v in adj[i]:
                if v != prev:
                    if not dfs(v, i):
                        return False

            return True            

        if not dfs(0, -1):
            return False

        return len(visited)==n


# 2-0-1-4        
#   |
#   3  


# dfs(0,-1)
# i = 0
# prev = -1
# visited = []      