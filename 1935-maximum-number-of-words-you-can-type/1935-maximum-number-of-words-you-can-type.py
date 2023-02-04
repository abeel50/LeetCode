class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(' ')
        
        res = 0
        for w in text:
            if all ([False for c in w if c in brokenLetters]):
                res += 1
        return res
                    
        