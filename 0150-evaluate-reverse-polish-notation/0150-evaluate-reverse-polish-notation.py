class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        st = []
        for c in tokens:
            if c not in ops:
                st.append(int(c))
            else:
                v2 , v1 = st.pop(), st.pop()
                if c == "+":
                    st.append(v1 + v2)
                elif c == "-":
                    st.append(v1 - v2)
                elif c == "*":
                    st.append(v1 * v2)
                else:
                    st.append(int(v1 / v2))
        return st[0]