class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r
        while l <= r:
            m = l + (r-l)//2
            if self.canFinishWithSpeed(m, piles, h):
                res = m
                r = m - 1
            else:
                l = m+1

        return res

    def canFinishWithSpeed(self, m: int, piles:List[int], h:int ):
        timetaken = 0       
        for p in piles:
            t = p//m if p%m==0 else p//m + 1
            timetaken += t
        return timetaken <= h             

        