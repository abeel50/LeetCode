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
        while l1 != None or l2 != None:
            if l1 is None:
                res = l2.val
            elif l2 is None:
                res = l1.val
            else:
                res = l1.val + l2.val
            if c == 1: res += 1
            if res > 9:
                res = int(str(res)[1])
                c = 1
            else:
                c = 0
            if head is None:
                head = ListNode(res)
                p = head
            else:
                p.next = ListNode(res)
                p = p.next
                
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if c == 1:
            p.next = ListNode(c)


            
        return head
        