class Solution:
    # store the (length + #) first so we always know that, and never even read the string after this number.

    def encode(self, strs: List[str]) -> str:
        if len(strs) is None:
            return ""

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res        

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res        
