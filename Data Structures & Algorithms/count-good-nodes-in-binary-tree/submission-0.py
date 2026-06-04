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
        self.res = 0
        self.dfs(root, [])
        return self.res

    def dfs(self, node, path):
        if not node:
            return
        if not path or node.val >= max(path):
            self.res += 1
        path.append(node.val)
        self.dfs(node.left, path)
        self.dfs(node.right, path)
        path.pop()
        return    

        