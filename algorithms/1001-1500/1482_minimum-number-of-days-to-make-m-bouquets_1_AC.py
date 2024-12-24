# medium
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
# if you're looking for some min/max and can't find any smart move, try binary search
from sortedcontainers import SortedSet

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        ll = min(bloomDay)
        rr = max(bloomDay)

        if self.search(ll, k, bloomDay) >= m:
            return ll

        while rr - ll > 1:
            mm = ll + (rr - ll >> 1)
            if self.search(mm, k, bloomDay) < m:
                ll = mm
            else:
                rr = mm
        return rr

    def search(self, d, k, a):
        b = [int(x <= d) for x in a]
        n = len(b)

        res = 0
        i = 0
        while i < n:
            if b[i] == 0:
                i += 1
                continue

            cc = 0
            while i < n and b[i] == 1:
                i += 1
                cc += 1
            res += cc // k

        return res
