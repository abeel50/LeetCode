class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d  ={"2":['a','b','c'], "3":['d','e','f'],
            "4":['g','h','i'], "5":['j','k','l'], "6":['m','n','o'],
            "7":['p','q','r','s'], "8":['t','u','v'], "9":['w','x','y','z']}
        if digits == "": return[]
        if len(digits) == 1: return d[digits]

        res = d[digits[0]]
        for i in range(1,len(digits)):
            res = [str(x) + str(y) for x in res for y in d[digits[i]]]
        
        return res