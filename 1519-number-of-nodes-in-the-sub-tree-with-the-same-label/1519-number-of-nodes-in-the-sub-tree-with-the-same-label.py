class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        
        tree = defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        
        res = [0] * n
        
        def dfs(node, par):
            count = Counter()
            for nei in tree[node]:
                if nei != par:
                    count += dfs(nei, node)
            
            count[labels[node]] += 1
            res[node] = count[labels[node]]
            
            return count
        
        dfs(0,-1)
        return res
        
            
        