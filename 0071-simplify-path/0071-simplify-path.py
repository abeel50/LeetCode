class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        res = ""
        
        for c in path + "/":
            if c == "/":
                if res == "..":
                    if st: 
                        st.pop()
                elif res != "" and res != ".":
                    st.append(res)
                res = ""
                
            else:
                res += c
        return "/" + "/".join(st)
        
                
            
        