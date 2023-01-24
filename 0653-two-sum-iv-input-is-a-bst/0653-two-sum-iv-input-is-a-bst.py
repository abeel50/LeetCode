# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        toFind= []
        def rec(root):
            if not root: return False
            nonlocal toFind
            
            if root.val in toFind:
                return True
            
            toFind.append(k - root.val)
            return rec(root.left) or rec(root.right)
        return rec(root)
            
        