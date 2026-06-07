class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(open_count, closed_count, cur):
            if open_count == closed_count == n:
                res.append(''.join(cur))
                return
            if open_count<n:
                cur.append('(')
                dfs(open_count+1, closed_count, cur)
                cur.pop()

            if closed_count < open_count:
                cur.append(')')
                dfs(open_count, closed_count+1, cur)      
                cur.pop()

        dfs(0, 0, [])
        return res          
        