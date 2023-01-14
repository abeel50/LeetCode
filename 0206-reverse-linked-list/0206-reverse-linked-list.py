# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(l1):
            if l1 == None:
                return None
            if l1.next == None:
                return l1
            temp = reverse(l1.next)
            p = temp
            while p.next != None:
                p = p.next
            p.next = ListNode(l1.val)
            return temp
            
        return(reverse(head))
        