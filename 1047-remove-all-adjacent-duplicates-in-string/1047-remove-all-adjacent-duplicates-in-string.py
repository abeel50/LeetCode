class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        
        for c in s:
            if len(st) > 0 and st[-1] == c:
                st.pop()
            else:
                st.append(c)
        return "".join(st)
        