class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][0] = min(res[-1][0], interval[0])
                res[-1][1] = max(res[-1][1], interval[1])

        return res        