class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == "+":
                st.append(st[-1] + st[-2])
            elif op == "D":
                st.append(st[-1] * 2)
            elif op == "C":
                st.pop()
            else:
                st.append(int(op))
        return sum(st)