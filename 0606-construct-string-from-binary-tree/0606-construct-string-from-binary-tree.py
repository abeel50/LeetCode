# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # to save strings
        res = []
        
        #recursive function
        def rec(root):
            if not root: return
            
            res.append("(")
            res.append(str(root.val))
            # parenthesis pairs that do not affect the one-to-one mapping 
            # relationship between the string and the original binary tree.
            # see example 2
            if not root.left and root.right:
                res.append("()")
            rec(root.left)
            rec(root.right)
            res.append(")")
            
        rec(root)
        return "".join(res[1:-1])    
        