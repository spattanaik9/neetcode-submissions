class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[-(x*x + y*y), (x,y)] for [x,y] in points ]
        
        maxheap = []
        heapq.heapify(maxheap)

        for d in dist:
            heapq.heappush(maxheap, d)
            if len(maxheap)>k:
                heapq.heappop(maxheap)

        res = []
        while len(maxheap)>0:
            val = heapq.heappop(maxheap)
            res.append(val[1])

        return res