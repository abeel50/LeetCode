class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = deque()
        self.history.append(homepage)
        self.curr = 0
        

    def visit(self, url: str) -> None:
        # print("Visit: ", url)
        for i in range(len(self.history)-1 , self.curr, -1):
            self.history.pop()
        self.history.append(url)
        self.curr += 1
        # print("history", self.history)
    
    def back(self, steps: int) -> str:
        # print("history", self.history)
        if self.curr - steps >= 0:
            self.curr -= steps
        else:
            self.curr = 0
        # print("Curr: " ,self.history[self.curr])
        return self.history[self.curr]
    
        

    def forward(self, steps: int) -> str:
        if self.curr + steps < len(self.history):
            self.curr += steps
        else:
            self.curr = len(self.history) - 1
        # print("Curr: ", self.history[self.curr])
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)