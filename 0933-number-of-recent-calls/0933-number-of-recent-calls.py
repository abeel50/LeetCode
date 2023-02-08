class RecentCounter:

    def __init__(self):
        self.reqs = defaultdict(bool)
        

    def ping(self, t: int) -> int:
        self.reqs[t] = True
        l, h = t - 3000, t
        return len([k for k in self.reqs.keys() if k >= l and k <= h])        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)