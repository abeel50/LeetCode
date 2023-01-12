# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #returns sum of grand Nodes
        def getSum(node):
            if node == None: return 0
            s, left, right =0, node.left, node.right
            if left != None: s += left.val
            if right != None: s+= right.val
            return s
                
        
        def helper(root):
            if root == None: return 0
            s = 0
            if root.val % 2 == 0:
                s = getSum(root.left) + getSum(root.right)
            return s + helper(root.left) + helper(root.right)
        
        return helper(root)
                
            
        