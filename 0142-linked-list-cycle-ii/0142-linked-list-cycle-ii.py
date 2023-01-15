# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = {}
 
        while(head != None):
            if head not in n.keys():
                n[head] = head.val
            else:
                return head
            head = head.next
        return None