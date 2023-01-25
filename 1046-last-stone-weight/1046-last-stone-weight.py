class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        heapify(heap)
        for s in stones:
            heappush(heap, s * -1)
            
        while len(heap) > 1:
            y = abs(heappop(heap))
            x = abs(heappop(heap))
            if y != x:
                heappush(heap, (y - x) * -1)
            
            
        return abs(heap[0]) if len(heap) > 0 else 0
        