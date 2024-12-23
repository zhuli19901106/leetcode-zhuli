# https://leetcode.com/problems/number-of-orders-in-the-backlog/
# nice question, this is actually the hello world of stock trading
# heaps, of course
from heapq import heappush, heappop

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = int(1e9 + 7)

        # max heap for buys
        buys = []
        # min heap for sells
        sells = []

        for p, q, ty in orders:
            # buy
            if ty == 0:
                while q > 0 and len(sells) > 0 and sells[0][0] <= p:
                    p1, q1 = heappop(sells)
                    if q < q1:
                        q1 -= q
                        q = 0
                    else:
                        q -= q1
                        q1 = 0

                    if q1 > 0:
                        heappush(sells, (p1, q1))

                if q > 0:
                    heappush(buys, (-p, q))
            # sell
            else:
                while q > 0 and len(buys) > 0 and -buys[0][0] >= p:
                    p1, q1 = heappop(buys)
                    p1 = -p1
                    if q < q1:
                        q1 -= q
                        q = 0
                    else:
                        q -= q1
                        q1 = 0

                    if q1 > 0:
                        heappush(buys, (-p1, q1))

                if q > 0:
                    heappush(sells, (p, q))

        res = 0
        for _, q in buys:
            res = (res + q) % MOD
        for _, q in sells:
            res = (res + q) % MOD
        return res
