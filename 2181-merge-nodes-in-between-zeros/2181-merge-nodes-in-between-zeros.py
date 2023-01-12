# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = head
        while p1 != None:
            if p1.val == 0:
                temp = p1.next
                if temp == None:
                    p2.next= None
                    break
                else:
                    while temp!= None and temp.val != 0:
                        p1.val += temp.val
                        temp = temp.next
                        p1.next = temp
                    p2 = p1 # pointer for last zero
                    p1 = temp
        return head
            
        