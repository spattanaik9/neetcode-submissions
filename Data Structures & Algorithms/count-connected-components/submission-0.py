class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.res = n
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for v in adj[i]:
                if v not in visited:
                    self.res -= 1
                    dfs(v)    

        for i in range(n):
            dfs(i)
        return self.res    
        
       