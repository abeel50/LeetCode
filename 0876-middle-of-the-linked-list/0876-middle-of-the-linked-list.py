# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result  = []
        temp = head
        while temp != None:
            result.append(temp)
            temp = temp.next

        return result[(len(result) // 2) ]
        
        