# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        def dfs(node):
            if not node: return 
            l = dfs(node.left)
            nodes.append(node.val)
            r = dfs(node.right)
        dfs(root)

        def build(l, r):
            if l > r: return 
            mid = l + (r - l) // 2
            node = TreeNode(nodes[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node

        return build(0, len(nodes) - 1)