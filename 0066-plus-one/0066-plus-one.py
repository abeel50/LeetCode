class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        c = 1
        i = len(digits) - 1

        while i >= 0:
            d = digits[i] + c
            c = 0
            if d > 9:
                digits[i] = d % 10
                c = d // 10
            else:
                digits[i] = d
                break
            i -= 1
        if c > 0:
            digits.insert(0, c)
        return digits
        