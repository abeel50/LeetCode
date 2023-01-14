# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        def mergeLists(l1,l2):
            temp = None
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            if l1.val <= l2.val:
                temp = ListNode(l1.val)
                temp.next = mergeLists(l1.next, l2)
            else:
                temp = ListNode(l2.val)
                temp.next = mergeLists(l1, l2.next)
            return temp
        return mergeLists(list1,list2)

                
                    
        