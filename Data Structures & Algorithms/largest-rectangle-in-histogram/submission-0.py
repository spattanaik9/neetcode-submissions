class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair of index, height

        for i, h in enumerate(heights):
            if not stack:
                stack.append([i, h])
            else:
                start = i
                while stack and stack[-1][1] > h:
                    stackIndex, stackHeight = stack.pop()
                    maxArea = max(maxArea, (i-stackIndex)*stackHeight)
                    start = stackIndex
                stack.append([start, h])

        for i, h in stack:
            maxArea = max(maxArea, (len(heights)-i)*h)

        return maxArea            

        