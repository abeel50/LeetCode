# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node == None: return 0
            return 1 + max(height(node.left),height(node.right))
             
        def helper(root):
            if root== None: return True
            lh = height(root.left) # gets left side height
            rh = height(root.right) #gets right side Height

            if abs(rh - lh) > 1: #if not returns False
                return False
            else:
                return True and helper(root.left) and helper(root.right) #recursive call
        return helper(root)
        