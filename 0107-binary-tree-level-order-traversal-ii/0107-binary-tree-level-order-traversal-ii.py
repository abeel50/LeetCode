# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def rec(root, level):
            if not root: return
            
            nonlocal res
            
            if len(res) > level:
                res[level].append(root.val)
            else:
                res.append([root.val])
                
            rec(root.left, level + 1)
            rec(root.right,level + 1)
            return
        
        rec(root, 0)
        print(res)
        return res[::-1]
            
                
        