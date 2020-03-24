# https://leetcode.com/problems/online-stock-span/
# use a min stack
class StockSpanner:
    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        res = 1
        st = self.st
        while len(st) > 0 and st[-1][0] <= price:
            res += st[-1][1]
            st.pop()
        st.append((price, res))
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
