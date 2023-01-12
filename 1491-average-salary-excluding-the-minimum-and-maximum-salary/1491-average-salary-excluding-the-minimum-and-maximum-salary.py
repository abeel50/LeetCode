class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
        mx, mn , s = salary[0], salary[0], 0
        for i in salary:
            s += i
            if i > mx:
                mx = i
            if i < mn:
                mn = i
        return (s - mx - mn) / float(len(salary) - 2)
        