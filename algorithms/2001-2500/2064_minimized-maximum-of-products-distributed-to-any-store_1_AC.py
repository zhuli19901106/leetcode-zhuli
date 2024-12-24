# medium
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
# binary search is a common trick for minimax problems
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # not that simple
        # return (sum(quantities) + n - 1) // n

        ll = 1
        rr = max(quantities)
        if self.distribute(quantities, 1) <= n:
            return 1

        while rr - ll > 1:
            mm = ll + (rr - ll >> 1)
            if self.distribute(quantities, mm) > n:
                ll = mm
            else:
                rr = mm
        return rr

    def distribute(self, qs, x):
        # luckily, the binary search criterion here is so simple
        res = 0
        for q in qs:
            res += (q + x - 1) // x
        return res
