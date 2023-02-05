class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.products = dict(zip(products, prices))
        self.nth = n
        self.discount = discount
        self.customerCounter = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customerCounter += 1
        total = sum ([self.products[product[i]] * amount[i] for i in range(len(product))])
        return total * ((100 - self.discount) / 100) if self.customerCounter % self.nth == 0 else total
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)