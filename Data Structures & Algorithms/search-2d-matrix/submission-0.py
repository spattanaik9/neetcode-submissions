class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l = 0
        r = rows*cols - 1

        while l <= r:
            m = l + (r-l)//2
            currow = m // cols
            curcol = m % cols

            if matrix[currow][curcol] == target:
                return True
            elif matrix[currow][curcol] < target:   
                l = m+1
            else:
                r = m-1

        return False            


      