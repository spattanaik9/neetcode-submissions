class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        tcounter = collections.defaultdict(int)
        scounter = collections.defaultdict(int)

        for c in t:
            tcounter[c]+=1

        need = len(tcounter)
        # print(need, tcounter)
        have = 0
        res, minlen, startindex, endindex = "", len(s)+1, 0, 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in tcounter:
                scounter[s[r]] += 1
                if scounter[s[r]] == tcounter[s[r]]:
                    have += 1
            while have == need:
                cur = r - l + 1
                if cur < minlen:
                    minlen = cur
                    startindex = l
                    endindex = r
                    res = s[l:r+1]

                if s[l] not in tcounter:
                    l += 1
                    continue
                scounter[s[l]] -= 1
                if scounter[s[l]] < tcounter[s[l]]:
                    have -= 1
                l += 1
            r += 1  
        return res                     

