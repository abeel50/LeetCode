# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result  = []
        temp = head
        while temp != None:
            result.append(temp)
            temp = temp.next

        return result[(len(result) // 2) ]
        