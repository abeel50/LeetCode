# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        self.cache = defaultdict(int)
        self.cache[targetSum] = 1

        def rec(node, rootSum):
            if not node: return
            
            rootSum += node.val
            self.res += self.cache[rootSum]
            self.cache[rootSum + targetSum] += 1
            
            rec(node.left, rootSum)
            rec(node.right, rootSum)
            self.cache[rootSum + targetSum] -= 1

        
        rec(root, 0)
        return self.res 