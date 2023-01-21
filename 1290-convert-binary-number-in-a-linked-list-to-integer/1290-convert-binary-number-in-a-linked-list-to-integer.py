# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # to save numbere 
        numbers = []
        
        #iterate through list 
        while head:
            # append numbers in list
            numbers.append(head.val)
            head = head.next
        res = 0
        
        # power of 2
        p = len(numbers) - 1
        
        for n in numbers:
            res += n * (2 ** p)
            p -= 1
        return res
            
            
        