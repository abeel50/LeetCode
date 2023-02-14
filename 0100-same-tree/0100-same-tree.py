# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            else:
                return (p.val == q.val ) and helper(p.left, q.left) and helper(p.right, q.right)
        return helper(p,q)
        