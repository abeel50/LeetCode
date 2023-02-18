class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] == ")":
                if st:
                    st.pop()
                else:
                    arr[i] = ""
            elif arr[i] == "(":
                st.append(i)
        
        for j in st:
            arr[j]=""
            
        return "".join(arr)
      