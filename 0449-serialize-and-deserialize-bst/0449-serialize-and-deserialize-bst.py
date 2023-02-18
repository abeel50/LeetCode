# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def rec(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            rec(node.left)
            rec(node.right)
        
        rec(root)
        return ",".join(res)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.idx = 0
        vals = data.split(",")
        
        def rec():
            if vals[self.idx] == "N":
                self.idx += 1
                return None
            node = TreeNode(int(vals[self.idx]))
            self.idx += 1
            
            node.left = rec()
            node.right = rec()
            return node
        
        return rec()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans