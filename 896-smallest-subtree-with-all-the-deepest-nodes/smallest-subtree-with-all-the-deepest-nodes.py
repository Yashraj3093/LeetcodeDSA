# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return (None,0)
            leftNode, leftDistance = dfs(node.left)
            rightNode, rightDistance = dfs(node.right)

            if leftDistance > rightDistance:
                return (leftNode, leftDistance + 1)

            elif rightDistance > leftDistance:
                return (rightNode, rightDistance + 1)
            
            else:
                return (node, leftDistance + 1)

        return dfs(root)[0]