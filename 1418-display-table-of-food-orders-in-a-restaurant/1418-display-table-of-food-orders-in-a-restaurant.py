from sortedcontainers import SortedDict, SortedSet

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = SortedDict()
        dishes = SortedSet()
        
        for c, t, d in orders:
            dishes.add(d)
            if int(t) not in tables:
                tables[int(t)] = defaultdict(int)
            tables[int(t)][d] += 1
            
        res = [["Table"] + list(dishes)]
        
        for k, v in tables.items():
            res.append([str(k)] + [str(v.get(d, "0")) for d in dishes])
        return res
        
            
        