class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        count = 0
        intervals.sort()
        for interval in intervals:
            if not res or res[-1][1] <= interval[0]:
                res.append(interval)
            else:
                if res[-1][1] >= interval[1]:
                    res[-1] = interval
                count += 1
        return count

