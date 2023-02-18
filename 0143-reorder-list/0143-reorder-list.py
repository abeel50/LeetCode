# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        # for splitting list in two halves
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #start of second half
        second = slow.next
        
        #seprate first half
        slow.next = None
        prv = None
        
        #reversing links of second half
        while second:
            temp = second.next
            second.next = prv
            prv = second
            second = temp
            
        first, second = head, prv
        
        #re arranging lists
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            
            first, second = temp1, temp2
            
            