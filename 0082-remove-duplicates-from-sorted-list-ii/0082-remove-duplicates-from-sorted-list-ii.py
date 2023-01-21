# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h = defaultdict(int)
        temp = head
        while temp:
            h[temp.val] += 1
            temp = temp.next
        res = None
        temp = None
        
        for k,v in h.items():
            if v == 1:
                if not res:
                    res = ListNode(k)
                    temp = res
                else:
                    temp.next = ListNode(k)
                    temp = temp.next
        return res
                