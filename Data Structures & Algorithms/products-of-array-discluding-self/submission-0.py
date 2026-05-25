class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]* len(nums)
        res = [1]*len(nums)

        curprod = 1
        
        for i in range(1, len(nums)):
            left[i] = nums[i-1]*curprod
            curprod = left[i]

        curprod = 1
        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1]*curprod  
            curprod = right[i]

        for i in range(len(nums)):
            res[i] = left[i]*right[i]

        return res            
        