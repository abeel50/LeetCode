# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        st = []
        temp = head
        while temp:
            st.append(temp.val)
            temp = temp.next
        
        res = float('-inf')
        while len(st) > 0:
            res = max(res, (st.pop(0) + st.pop()))
        return res
        