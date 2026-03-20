# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0 
        def traversal(node, depth):
            nonlocal max_depth   
            if not node:
                max_depth = max(max_depth, depth)
                return
            traversal(node.left, depth + 1)
            traversal(node.right, depth + 1)
        traversal(root, 0)
        return max_depth