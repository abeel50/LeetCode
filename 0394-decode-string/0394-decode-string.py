class Solution:
    def decodeString(self, s: str) -> str:
        
        st = []
        
        for c in s:
            if c != "]":
                st.append(c)
            else:
                # to get expression inside beackets
                exp = ""
                while st[-1] != "[":
                    exp = st.pop() + exp
                st.pop()
                # for k digit
                k = ""
                while st and st[-1].isdigit():
                    k = st.pop() + k
                # appedn to stack
                st.append(int(k) * exp)
        return "".join(st)
                
                
            
        