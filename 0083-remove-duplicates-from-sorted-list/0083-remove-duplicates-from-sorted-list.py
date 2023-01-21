# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        
        while temp:
            p = temp.next
            while p and temp.val == p.val:
                temp.next = p.next
                p = p.next
            temp = temp.next
        return head
        