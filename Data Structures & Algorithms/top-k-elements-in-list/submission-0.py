class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = []
        for f, v in count.items():
            freq.append([v, f])

        freq.sort()

        res = []
        while len(res)<k:
            res.append(freq.pop()[1])
        return res            
        