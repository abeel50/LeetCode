class Solution:
    def isValid(self, s: str) -> bool:
        start =['(','{','[']
        st = []
        for i in s:
            if i in start:
                st.append(i)
            elif len(st) == 0:
                return False
            elif i == ')' and st.pop() != '(':
                return False
            elif i == '}' and st.pop() != '{':
                return False
            elif i == ']' and st.pop() != '[':
                return False
        return len(st) == 0
        