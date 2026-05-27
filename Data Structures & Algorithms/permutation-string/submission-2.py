class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1count = collections.defaultdict(int)
        s2count = collections.defaultdict(int)
        
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')] += 1
            s2count[ord(s2[i])-ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        if s1count == s2count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # move left
            s2count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            #move right
            s2count[ord(s2[r]) - ord('a')] += 1
            
            if s1count == s2count:
                return True

        return s1count == s2count          


