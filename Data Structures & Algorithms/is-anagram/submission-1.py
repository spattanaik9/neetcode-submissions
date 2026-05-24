class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # 1. create a hashmap. and iterate for the 2ns string
        # #T:O(n)
        # #S:O(n)
        # if s is None or t is None or len(s)!=len(t):
        #     return False

        # hashmap = {}
        # for c in s:
        #     if c not in hashmap:
        #         hashmap[c] = 1
        #     else:
        #         hashmap[c] += 1

        # for c in t:
        #     if c not in hashmap or hashmap[c] <=0:
        #         return False
        #     hashmap[c] -= 1

        # for k, v in hashmap.items():
        #     if v != 0:
        #         return False

        # return True

        # 2. sorting
        if s is None or t is None or len(s) != len(t):
            return False

        return sorted(s)==sorted(t)    