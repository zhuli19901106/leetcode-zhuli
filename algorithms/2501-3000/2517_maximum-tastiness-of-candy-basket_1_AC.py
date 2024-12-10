# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/
# binary search, a bit challenging on the idea
# don't forget boundary checks
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        ll, rr = 0, price[-1] - price[0]
        if self.checkTastiness(price, rr) >= k:
            return rr

        while rr - ll > 1:
            mm = ll + (rr - ll >> 1)
            cc = self.checkTastiness(price, mm)
            if cc < k:
                rr = mm
            else:
                ll = mm
        return ll

    def checkTastiness(self, price, t):
        cur = -t
        k = 0
        for x in price:
            if cur + t <= x:
                cur = x
                k += 1
        return k
