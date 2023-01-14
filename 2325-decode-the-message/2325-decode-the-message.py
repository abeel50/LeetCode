class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        d = {}
        i = 0
        for k in key:
            if len(d.keys()) == 26:
                break  
            if k!= " " and k not in d.keys():
                d[k] = string.ascii_lowercase[i]
                i += 1
        d[" "] = " "
        decoded = ""
        for m in message:
            decoded += d[m]
        return decoded

        