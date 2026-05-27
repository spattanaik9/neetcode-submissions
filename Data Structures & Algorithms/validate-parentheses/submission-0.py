class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        } 
        stack = []
        for c in s:
            if c in brackets:
                if not stack:
                    return False
                elif stack[-1]!=brackets[c]:    
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return len(stack)==0
                    
        