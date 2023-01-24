# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(root):
            if not root:
                root = TreeNode(val)
                return root
            if val < root.val:
                root.left = insert(root.left)
            else:
                root.right = insert(root.right)
            return root
        root = insert(root)
        return root
                
                
            
        