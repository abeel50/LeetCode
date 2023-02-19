class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(l, r, s):
            if l == 0 and r == 0:
                res.append(s)
            if l > 0:
                dfs(l - 1, r, s + '(')
            if l < r:
                dfs(l, r - 1, s + ')')

        dfs(n, n, '')
        return res
        