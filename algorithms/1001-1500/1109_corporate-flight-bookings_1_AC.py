# https://leetcode.com/problems/corporate-flight-bookings/
# BIT solution, very intuitive if you're OK with writing it
class BIT:
    '''Fenwick tree for range add and single query
    '''
    def __init__(self, n):
        self.n = n
        self.a = [0 for i in range(n + 1)]

    def add(self, val, i, j=None):
        if not j is None:
            self.add(-val, i - 1)
            self.add(val, j)
            return

        n = self.n
        a = self.a
        if i < 1 or i > n:
            return
        idx = i
        while idx > 0:
            a[idx] += val
            idx = (idx & idx - 1)

    def query(self, i):
        n = self.n
        a = self.a
        if i < 1 or i > n:
            return
        idx = i
        val = 0
        while idx <= n:
            val += a[idx]
            idx += (idx & -idx)
        return val

    def __str__(self):
        res = []
        for i in range(self.n):
            res.append(self.query(i + 1))
        return str(res)

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bit = BIT(n)
        for b in bookings:
            bit.add(b[2], b[0], b[1])
        res = []
        for i in range(n):
            res.append(bit.query(i + 1))
        return res
