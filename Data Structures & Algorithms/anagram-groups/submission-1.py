class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. sorting
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)

        # return list(res.values())
        #T: O(n*mlogm)
        #S: O(n*m)
        #n: number of elements in strs, and m is max length of strings in strs

        #2. hashmap of alpabet, no sorting
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())   

        #n: len of strs, m is max len of string in strs
        #T: O(n*m)
        #S: O(n*m)     keys =  max keys is n, each take 26 chars, so O(n). values are O(n.k), so space = O(n.k)

        