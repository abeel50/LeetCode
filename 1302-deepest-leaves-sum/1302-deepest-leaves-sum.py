# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Recursive function to find depth of Tree
        def findDepth(root):
            if root == None: return 0
            return 1 + max(findDepth(root.left), findDepth (root.right))
        
        depth = findDepth(root)
    
        def sumOfDepth(root, d = 0):
            if root == None: return 0 
            if d == depth: #if on desired depth
                return root.val
            else: #oterwise go for next depth
                return sumOfDepth(root.left, d + 1) + sumOfDepth(root.right, d + 1)
        return sumOfDepth(root,1)

                
        