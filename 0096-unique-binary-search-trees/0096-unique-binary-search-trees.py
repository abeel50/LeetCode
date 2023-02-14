class Solution:
    def numTrees(self, n: int) -> int:
        numTrees = [1] * (n + 1)
        
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left, right = root - 1, nodes - root
                total += numTrees[left] * numTrees[right]
            numTrees[nodes] = total
        return numTrees[n]