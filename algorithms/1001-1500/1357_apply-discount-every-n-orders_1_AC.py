# medium
# https://leetcode.com/problems/apply-discount-every-n-orders/
class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n_dis = n
        self.dis = discount
        pr = {}
        np = len(products)
        for i in range(np):
            pr[products[i]] = prices[i]
        self.pr = pr
        self.idx = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        res = 0
        n = len(product)
        for i in range(n):
            res += self.pr[product[i]] * amount[i]
        self.idx += 1
        if self.idx == self.n_dis:
            res = res * (1 - self.dis / 100.0)
            self.idx = 0
        return res

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)