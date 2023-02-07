# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n = {}
        while head:
            if head not in n.keys():
                n[head] = head.val
            else:
                return head
            head = head.next
        return None
        