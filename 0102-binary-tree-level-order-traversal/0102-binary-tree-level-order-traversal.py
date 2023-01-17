# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        def helper(btNode, level):
            if btNode is None: return
            #if level array has not been inserted yet
            if not( level < len(res)):
                res.append([])
            #append current Node in it's level
            res[level].append(btNode.val)

            helper(btNode.left, level+1)
            helper(btNode.right, level+1)
        helper(root,0)
        return res
            