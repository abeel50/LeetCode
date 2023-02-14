class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        two, three, five = 0, 0, 0
        
        # check hint 4
        #Assume you have Uk, the kth ugly number.
        #Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5)
        while len(ugly) < n:
            while ugly[two] * 2 <= ugly[-1]:
                two += 1
            while ugly[three] * 3 <= ugly[-1]:
                three += 1
            while ugly[five] * 5 <= ugly[-1]:
                five += 1
            ugly.append(min(ugly[two] * 2, ugly[three] * 3, ugly[five] * 5))
        
        return ugly[-1]  
        