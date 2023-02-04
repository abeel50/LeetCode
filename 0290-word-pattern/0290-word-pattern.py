class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d = {}
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d.keys():
                if d[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in d.values():
                    return False
                else:
                    d[pattern[i]] = s[i]
        return True
