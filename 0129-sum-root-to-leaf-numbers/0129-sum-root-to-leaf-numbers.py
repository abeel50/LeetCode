# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def rec(root, curPath):
            if not root: return
            
            curPath.append(str(root.val))
            if not root.left and not root.right:
                self.res += int(''.join(curPath))
            else:
                rec(root.left, curPath[:])
                rec(root.right, curPath[:])
        
        rec(root, [])
        return self.res
        