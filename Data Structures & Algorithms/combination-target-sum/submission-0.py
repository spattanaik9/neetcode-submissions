class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        cur = []

        def dfs(i, total):
            if i >= len(nums) or total>target:
                return 
            if total == target:
                res.append(cur.copy())
                return 
            #take it
            cur.append(nums[i])
            dfs(i, total+nums[i])

            #dont take it
            cur.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return res    




        