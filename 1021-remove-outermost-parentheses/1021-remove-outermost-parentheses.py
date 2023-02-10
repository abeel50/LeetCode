class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []        
        res = ""
        # fort count of "("
        count = 0
        
        for c in s:
            st.append(c)
            if c == "(":
                count += 1 
            if c == ")" and len(st) ==  2 * count:
                #remove outer paranthesis
                st.pop()
                st.pop(0)
                res += "".join(st)
                st = []
                count = 0
                
        return res
            