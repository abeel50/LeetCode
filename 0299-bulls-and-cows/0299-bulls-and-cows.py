class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        h_sec, h_guess = defaultdict(int) , defaultdict(int)
        for c in secret:
            h_sec[c] += 1
        for c in guess:
            h_guess[c] += 1
            
        bulls ,cows = 0, 0
        
        for i in range(len(guess)):
            s, g = secret[i], guess[i]
            if g == s:
                bulls += 1
                h_sec[s] -= 1
                h_guess[g] -= 1
                
                if h_sec[s] <= 0:
                    del h_sec[s]
                if h_guess[g] <= 0:
                    del h_guess[g]
                
        for k, v in h_guess.items():
            if k in h_sec:
                cows += min(v, h_sec[k])
            

        return str(bulls) + "A" + str(cows) +"B"
                
            
                
        