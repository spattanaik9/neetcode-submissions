class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            j = i+1
            while j< len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
                j += 1
            if j == len(temperatures):
                res.append(0)  

        return res          
        

        