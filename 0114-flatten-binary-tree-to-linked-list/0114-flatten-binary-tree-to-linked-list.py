# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def rec(root):
            if not root: return None
            
            #traverse to last subtree first
            if root.left:
                root.left = rec(root.left)
            if root.right:
                root.right = rec(root.right)
                
            # if node has both left and right child
            if root.left and root.right:
                #temp store curr right side
                temp = root.right
                #put left side to right
                root.right = root.left
                # left is None now
                root.left = None
                # pointer to travel to last of newly added portion
                tempNode = root.right
                while tempNode.right:
                    tempNode = tempNode.right
                #place original right side
                tempNode.right = temp
                
            # if there's no right side simply put left to right
            elif root.left and not root.right:
                root.right = root.left
                root.left = None
                
            return root
        return rec(root)
        
        