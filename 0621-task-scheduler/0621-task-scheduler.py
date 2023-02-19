class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = defaultdict(int)
        for t in tasks:
            h[t] += 1
            
        maxHeap = [-c for c in h.values()]
        heapq.heapify(maxHeap)
        time = 0
        
        #(-c, idleTime)
        q = deque() 
        
        while maxHeap or q:
            time += 1 
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time   