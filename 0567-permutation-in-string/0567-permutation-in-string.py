class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = {}
        s2_counter = {}
        for i in range(26):
            s1_counter[chr(ord('a') + i)] = 0
            s2_counter[chr(ord('a') + i)] = 0
        for i in range(len(s1)):
            s1_counter[s1[i]] += 1
            s2_counter[s2[i]] += 1

        for i in range(len(s1), len(s2)):
            if s1_counter == s2_counter:
                return True
            s2_counter[s2[i]] += 1
            s2_counter[s2[i - len(s1)]] -= 1
        return s1_counter == s2_counter
