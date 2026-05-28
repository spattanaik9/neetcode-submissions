class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l)//2
            if nums[m]==target:
                return m

            if nums[l]<=nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[m] <= nums[r]:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1                            
        