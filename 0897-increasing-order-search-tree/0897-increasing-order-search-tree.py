# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inOrder = []
        def rec(root):
            if not root: return
            nonlocal inOrder
            rec(root.left)
            inOrder.append(root.val)
            rec(root.right)
        rec(root)
        
        def build(root, idx):
            if idx >= len(inOrder): return None
            
            root = TreeNode(inOrder[idx])
            root.right = build(root.right, idx + 1)
            return root
            
        newRoot = build(None, 0)
        return newRoot
        
