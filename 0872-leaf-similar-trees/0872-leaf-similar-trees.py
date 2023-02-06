# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def rec(root, leafs):
            if not root: return
            
            if not root.left and not root.right:
                leafs.append(root.val)
            rec(root.left, leafs)
            rec(root.right, leafs)
        
        leaf1, leaf2 = [], []
        
        rec(root1, leaf1)
        rec(root2, leaf2)
        
        if len(leaf1) != len(leaf2):
            return False
        
        return all([leaf1[i] == leaf2[i] for i in range(len(leaf1))])

        