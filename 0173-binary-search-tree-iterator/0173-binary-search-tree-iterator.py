# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inOrder = [-1]
        self.pointer = 0
        self.rec(root)
        
    def rec(self,root):
        if not root: return
        self.rec(root.left)
        self.inOrder.append(root.val)
        self.rec(root.right)
        

    def next(self) -> int:
        self.pointer += 1
        return self.inOrder[self.pointer]
        

    def hasNext(self) -> bool:
        return True if (self.pointer + 1) < len(self.inOrder) else False
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()