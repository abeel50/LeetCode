class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        # hashTable to store occurence of char
        h = defaultdict(int)
        
        #max length to keep track of longest substring
        maxLength = 0
        start, end = 0, 0
        
        for i, c in enumerate(s):
            #if char is alreday in hash
            #that means ther's repeation
            if c in h:
                maxLength = max(maxLength, (end - start) + 1) #compute max of curr substring
                if h[c] + 1 > start:
                    start = h[c] + 1
                del h[c]   
            h[c] = i
            end = i
            # print(h)
            # print(start, end, maxLength)
        
        return max(maxLength, (end - start) + 1)

                
                
            
        