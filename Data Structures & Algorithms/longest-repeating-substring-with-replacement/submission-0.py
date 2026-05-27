class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hashmap = {}
        maxf = 0
        res = 0

        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxf = max(maxf, hashmap[s[r]])
            if (r-l+1 - maxf)>k:
                hashmap[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        
        return res


# XYYXXZY

# {X:2, Y:3, Z:1}
# l=1, r=6
# maxf = 3
# res = 5

        