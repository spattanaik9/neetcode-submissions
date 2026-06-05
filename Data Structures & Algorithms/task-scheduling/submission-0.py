class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [ -cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()
        while maxheap or q:
            time += 1

            if maxheap:
                cur = heapq.heappop(maxheap) + 1
                if cur != 0:
                    q.append([cur, time+n])

            if q and q[0][1]<=time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time        


        