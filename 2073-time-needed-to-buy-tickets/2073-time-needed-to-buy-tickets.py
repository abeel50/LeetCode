class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        q = deque([*range(len(tickets))])
        
        while q:
            p = q.popleft()
            tickets[p] -= 1
            time += 1
            if tickets[p] != 0:
                q.append(p)
            if p == k and tickets[p] == 0:
                break
        return time
            
            
        