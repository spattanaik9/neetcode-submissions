class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True

        return False        


# 1. sort. T-O(nlogn), S-O(1)
# 2. hashmap. T-O(n), S-O(n)        
        