# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def rec(node, level):
            if not node: return 
            if len(res) <= level:
                res.append([])
            
            rec(node.left, level + 1)
            rec(node.right, level + 1)
            
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
        
        rec(root, 0)
        return res
            
                
        