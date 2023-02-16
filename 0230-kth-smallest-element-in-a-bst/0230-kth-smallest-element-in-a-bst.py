# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inOrder = []
        def rec(root):
            if not root: return
            rec(root.left)
            inOrder.append(root.val)
            rec(root.right)
            
        rec(root)        
        return inOrder[k-1]
            
        