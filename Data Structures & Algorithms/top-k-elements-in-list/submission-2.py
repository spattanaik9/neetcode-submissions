class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        bucket = [[] for i in range(len(nums)+1)]
        for n, freq in count.items():
            bucket[freq].append(n)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res