# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p1 = head
        while head and head.val == val:
            head = head.next
        p2 = None
        
        while p1 and p1.next is not None:
            if p1.next.val == val:
                p2 = p1.next
                while p2 and p2.val == val:
                    p2 = p2.next
                p1.next = p2
            p1 = p1.next
        return head
        