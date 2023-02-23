class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = {5:0, 10:0, 20:0}
        for b in bills:
            if b == 5:
                notes[5] += 1
            elif b == 10 and notes[5] > 0:
                notes[5] -= 1
                notes[10] += 1
            elif b == 20 and notes[10] > 0 and notes[5] > 0:
                notes[5] -= 1
                notes[10] -= 1
                notes[20] += 1
            elif b == 20 and notes[10] == 0 and notes[5] >= 3:
                notes[5] -= 3
                notes[20] += 1
            else:
                return False
        return True
            
        