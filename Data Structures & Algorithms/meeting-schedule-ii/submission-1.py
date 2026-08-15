"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minheap = []
        intervals.sort(key = lambda x: (x.start, x.end))
        maxrooms = 0
        for interval in intervals:
            while minheap and minheap[0] <= interval.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, interval.end)
            maxrooms = max(maxrooms, len(minheap))
        return maxrooms    



        