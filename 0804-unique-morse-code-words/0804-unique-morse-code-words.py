class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
                 ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
                 ".--","-..-","-.--","--.."]
        morseCode = dict(zip(string.ascii_lowercase, codes))
        res = set()
        
        for w in words:
            res.add("".join([morseCode[c] for c in w]))
        return len(res)
        