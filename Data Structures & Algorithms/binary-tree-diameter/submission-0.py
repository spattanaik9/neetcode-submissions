# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            maxleft = dfs(node.left)
            maxright = dfs(node.right)
            res = max(res, maxleft+maxright)
            return max(maxleft, maxright)  +1  

        dfs(root)
    
        return res        


        