# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def helper(p,q):
            if p is None and q is None:
                return True
            if p == None or q == None or p.val != q.val:
                return False
            else:
                return (p.val == q.val ) and helper(p.left,q.left) and helper(p.right,q.right)
        return helper(p,q)
            
