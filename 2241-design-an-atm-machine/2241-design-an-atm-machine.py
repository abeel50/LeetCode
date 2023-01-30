class ATM:

    def __init__(self):
        self.bank_notes = {20:0, 50:0, 100:0, 200:0, 500:0}
        

    def deposit(self, banknotesCount: List[int]) -> None:
        i = 0
        for k in self.bank_notes.keys():
            self.bank_notes[k] += banknotesCount[i]
            i += 1
        
    def withdraw(self, amount: int) -> List[int]:

        notes = [0,0,0,0,0]
        idx = 4
        for k in reversed(self.bank_notes.keys()):
            if amount >= k:
                c = amount // k
                if c > self.bank_notes[k]:
                    c = self.bank_notes[k]
                self.bank_notes[k] -= c
                amount -= c * k
                notes[idx] = c
            idx -= 1
        
        if amount == 0: return notes
        else:
            for i, k in enumerate(self.bank_notes.keys()):
                self.bank_notes[k] += notes[i]
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)