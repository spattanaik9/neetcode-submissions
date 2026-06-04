# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.dfs(root, root.val)

    def dfs(self, node, max_val):
        if not node:
            return 0
        res = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        return res + self.dfs(node.left, max_val) + self.dfs(node.right, max_val)
#T: n*n
#S: n
        