# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mindepth = float('inf')
        def dfs(node, depth):
            nonlocal mindepth
            if not node:
                return
            depth += 1
            dfs(node.left,depth)
            dfs(node.right, depth)
            if not node.left and not node.right:
                mindepth = min(mindepth, depth)
        
        dfs(root, 0)
        return mindepth
        