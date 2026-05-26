class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in hashmap:
                l = max(l, hashmap[s[r]]+1)
                hashmap.pop(s[r])

            hashmap[s[r]] = r
            res = max(res, r-l+1)
            r += 1
            
        return res    

# abba

# l=2,r=3 
# hashmap={
# a:0, b:2
# }
# res = 2
        