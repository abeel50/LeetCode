class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0: return True
        i, j ,match= 0, 0, 0
        while i< len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                match += 1
            j += 1
        return len(s) == match
        
            
        