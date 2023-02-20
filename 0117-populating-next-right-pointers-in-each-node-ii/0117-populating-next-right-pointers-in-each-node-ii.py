"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        if root:
            q.append((root, 0))
        while q:
            node, level = q.popleft()
            
            # if nodes are on same level
            if len(q) > 0:
                nextNode, nextLevel = q[0]
                if level == nextLevel:
                    node.next = nextNode
            
            for nextNode in [node.left, node.right]:
                if nextNode:
                    q.append((nextNode, level + 1))
                    
        return root
        