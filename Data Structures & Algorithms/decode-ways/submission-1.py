class Solution:
    def numDecodings(self, s: str) -> int:
        def solve(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if t[i] != 0:
                return t[i]
            res = solve(i+1)

            if (i+1 < len(s) and (
                s[i]=='1' or 
                (s[i]=='2' and s[i+1] in '0123456')
            )):
                res += solve(i+2)

            t[i] = res
            return res
        t = [0]*len(s)
        return solve(0)                
        