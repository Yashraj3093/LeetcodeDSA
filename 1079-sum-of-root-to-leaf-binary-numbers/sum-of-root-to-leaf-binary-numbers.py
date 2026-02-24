# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node,b):
            b <<= 1
            b |= node.val

            if not node.left and not node.right:
                self.result += b
                return 

            if node.left: dfs(node.left,b)
            if node.right: dfs(node.right,b)

        dfs(root,0)
        return self.result