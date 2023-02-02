# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # queue for saving elements
        st = deque()
        temp = head
        # append all elements
        while temp:
            st.append(temp.val)
            temp = temp.next
        if len(st) == 1 : return True
        # till queue is not empty
        while st:
            if st[0] != st[-1]:
                return False
            elif len(st) == 1 and st[0] == st[-1]:
                break
            else:
                st.popleft() #pop from front
                st.pop() # pop from end
        return True
        