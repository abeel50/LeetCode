# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        p = None
        c = 0
        while l1 or l2:
            if not l1:
                res = l2.val + c
            elif not l2:
                res = l1.val + c
            else:
                res = l1.val + l2.val + c
                
            # if ther's a carry
            if res > 9:
                res = int(str(res)[1])
                c = 1
            else:
                c = 0
                
            if not head:
                head = ListNode(res)
                p = head
            else:
                p.next = ListNode(res)
                p = p.next
                
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if c == 1:
            p.next = ListNode(c)

        return head
        