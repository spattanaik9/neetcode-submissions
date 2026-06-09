class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {
            i : [] for i in range(numCourses)
        }

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if len(pre_map[crs])==0:
                return True

            visited.add(crs)
            for p in pre_map[crs]:
                if not dfs(p):
                    return False
            pre_map[crs] = []
            visited.remove(crs)
            return True        

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True            
        