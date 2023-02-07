class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefix = []
        self.k = 1
        

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = []
            return
        if num != 1:
            for i in range (len(self.prefix)):
                self.prefix[i] *= num
        self.prefix.append(num)
        

    def getProduct(self, k: int) -> int:
        if k <= len(self.prefix):
            return self.prefix[len(self.prefix) - k]
        else:
            return 0
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)