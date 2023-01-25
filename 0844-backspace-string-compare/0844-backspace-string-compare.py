class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        st, st2 = [], []
        
        for c in s:
            if c == "#":
                if len(st) != 0:
                    st.pop()
            else:
                st.append(c)
        for c in t:
            if c == "#":
                if len(st2) != 0:
                    st2.pop()
            else:
                st2.append(c)
        if len(st) != len(st2): return False
        
        for i in range(len(st)):
            if st[i]!= st2[i]:
                return False
        return True
                
        