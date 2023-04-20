# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = [(root, 0)]
        res = 1
        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            tmp = []
            for node, pos in q:
                if node.left:
                    tmp.append((node.left, pos * 2))
                if node.right:
                    tmp.append((node.right, pos * 2 + 1))
            q = tmp
        return res