# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        s = 0
        def rec(root):
            if not root: return 0
            nonlocal s
            if root.val >= low and root.val <= high:
                s += root.val
                rec(root.left)
                rec(root.right)
            elif root.val < low:
                rec(root.right)
            else:
                rec(root.left)

        rec(root)
        return s