# medium
# https://leetcode.com/problems/product-of-the-last-k-numbers/
# 1AC, clear on zero
class ProductOfNumbers:
    def __init__(self):
        self.q = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.q = [1]
        else:
            self.q.append(self.q[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.q) - 1
        if n < k:
            return 0
        return self.q[n] // self.q[n - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)