class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]    
        
        prev1, prev2 = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            
            cur = max(prev1+nums[i], prev2)
            
            prev1 = prev2
            prev2 = cur

        return max(prev1, prev2)
        