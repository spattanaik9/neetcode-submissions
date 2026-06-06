class MedianFinder:

    def __init__(self):
        self.lo = [] #maxheap
        self.hi = [] #minheap
        

    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi):
            heapq.heappush(self.lo, -num)
            ele = heapq.heappop(self.lo)
            heapq.heappush(self.hi, -ele)
        else:
            heapq.heappush(self.hi, num)
            ele = heapq.heappop(self.hi)
            heapq.heappush(self.lo, -ele)    
        

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0])/2
        else:
            return self.hi[0]    
