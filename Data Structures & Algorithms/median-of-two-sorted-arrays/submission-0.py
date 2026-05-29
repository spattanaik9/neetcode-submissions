class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #    run a binary search on smaller array to see how many elements we need to take from it
        if len(nums2)<len(nums1):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1)+len(nums2)

        l, r = 0, len(nums1)-1

        while True:
            ma = (l+r)//2
            mb = total//2 -ma - 2
            # allocate the boundary elements
            Aleft = nums1[ma] if ma >=0 else float('-inf')
            Aright = nums1[ma+1] if ma+1 < len(nums1) else float('inf') 
            Bleft = nums2[mb] if mb >= 0 else float('-inf')
            Bright = nums2[mb+1] if mb+1 < len(nums2) else float('inf')

            # check if boundary is valid, or move it
            if Aleft<=Bright and Bleft<=Aright:
                #if total length is odd, median is in right part
                if total%2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft)+min(Aright, Bright))/2

            elif Aleft > Bright:
                r = ma-1
            else:
                l = ma+1                




        