# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def rec(node, st):
            if len(st) == 0: return None
            left, right = [], []
            root = st[0]
            
            for i in range(1, len(st)):
                if st[i] < root:
                    left.append(st[i])
                else:
                    right.append(st[i])
                    
            node = TreeNode(root)
            node.left = rec(node.left, left)
            node.right = rec(node.right, right)
            return node

        
        head = rec(None, preorder)
        return head