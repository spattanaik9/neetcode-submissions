class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums)==1:
            return nums[0]    


        return max(self.rob_util(nums[:-1]), self.rob_util(nums[1:]))

    def rob_util(self, nums):
        if len(nums)==1:
            return nums[0]

        one = nums[0]
        two = max(nums[0], nums[1])
        for n in nums[2:]:
            one, two = two, max(two, one + n)

        return two        

        