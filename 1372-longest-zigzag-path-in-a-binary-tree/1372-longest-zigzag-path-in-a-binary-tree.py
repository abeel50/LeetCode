# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.path = 0
        def helper(node, left, steps):
            if node:
                self.path = max(self.path, steps)
                if left:
                    helper(node.left, False, steps + 1)
                    helper(node.right, True, 1)
                else:
                    helper(node.left, False, 1)
                    helper(node.right, True, steps + 1)
                
        helper(root, False, 0)
        helper(root, True, 0)
        return self.path
        