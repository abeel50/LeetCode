# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # return pair: [withRoot, withoutRoot]
        def dfs(root):
            #Base case
            if not root:
                return [0, 0]
            
            #dfs calls
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)
            
            #if including current Node 
            # return pair: [withRoot, withoutRoot]
            # we can't use with root value of it's children
            withRoot = root.val + leftPair[1] + rightPair[1]
            
            #if we don't include root Value
            # then we get max from left subTree + max from right subTree
            withoutRoot = max(leftPair) + max(rightPair)
            
            return [withRoot, withoutRoot]
        return max(dfs(root))
            
        