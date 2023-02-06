# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        sums = []
        
        def rec(root, level):
            if not root: return
            
            if len(sums) < level:
                sums.append([root.val])
            else:
                sums[level-1].append(root.val)
            
            rec(root.left, level + 1)
            rec(root.right, level + 1)
        rec(root, 1)
        
        return [mean(l) for l in sums]
            
            
        