# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rec(p1, p2):
            if not p1 and not p2: return None
            if p1 and not p2: return p1
            
            p1.next = p2.next
            p2.next = p1
        
            res = p2
                        
            p1 = p1.next if p1 else None
            p2 = p1.next if p1 else None
            
            res.next.next = rec(p1,p2)
            return res
        
        return rec(head, head.next if head else None)
