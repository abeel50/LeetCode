class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        h = defaultdict(int)
        for w in words:
            h[w] += 1
        heap= []
        
        for key, v in h.items():
            heapq.heappush(heap, (-1*v,key))

        return [(heappop(heap))[1]  for i in range(k)]
