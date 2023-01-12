class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        group = defaultdict(list)
        res =[]
        for i in range(len(groupSizes)):
            g = groupSizes[i]
            if g in group.keys():
                if len(group[g]) == g:
                    res.append(group[g])
                    group[g] = [i]
                else:
                    group[g].append(i)
            else:
                group[g].append(i)

        for v in group.values():
            if len(v) > 0: 
                res.append(v)
        return res
        