class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct: return 0
        #split string to get hours and minutes
        [h, m]= current.split(":")
        [h1,m1] = correct.split(":")
        
        #converts time to minutes
        current, correct = int(h) * 60  + int(m), int(h1) * 60  + int(m1)
        
        diff = correct - current
        ops = 0
        while diff != 0:
            #60 minutes
            h, diff = divmod(diff, 60)
            ops += h
            
            #15 minutes
            m15, diff = divmod(diff, 15)
            ops += m15
            
            #5 minutes
            m5, diff = divmod(diff, 5)
            ops += m5
            
            #1 minute
            m1, diff = divmod(diff, 1)
            ops += m1
            
        
        return ops
        