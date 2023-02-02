class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # if length of substring is enough for matching the word
                # and sub string is a word from dict
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                    
                #if found a word in string no need to check other words in dict
                if dp[i]:
                    break
        return dp[0]
                
            