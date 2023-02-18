# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy  = ListNode(-1, head)
        groupPrv = dummy
        
        while True:
            kth = self.getKth(groupPrv, k)
            if not kth:
                break
            groupNext = kth.next
            
            prv, cur = kth.next, groupPrv.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prv
                prv = cur
                cur = temp
            
            tmp = groupPrv.next
            groupPrv.next = kth
            groupPrv = tmp
            
        return dummy.next
 