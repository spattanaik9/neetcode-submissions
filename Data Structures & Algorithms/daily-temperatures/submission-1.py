class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:
                stackind, stacktemp = stack.pop()
                res[stackind] = i-stackind
            stack.append([i, temp])
        

        return res          
        

        