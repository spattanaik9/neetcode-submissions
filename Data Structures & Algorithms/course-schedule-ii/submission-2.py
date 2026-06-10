class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        visiting = set()
        res = []

        #create adj list
        adj = { i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True

            visiting.add(i)

            for v in adj[i]:
                if not dfs(v):
                    return False

            visiting.remove(i)
            visited.add(i)  
            res.append(i)
            return True      
                    

        #iterate thru all courses and dfs
        for i in range(numCourses):
           if not dfs(i):
                return []

        return res        
