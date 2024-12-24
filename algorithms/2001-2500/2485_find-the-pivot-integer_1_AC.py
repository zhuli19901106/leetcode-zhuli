# easy
# https://leetcode.com/problems/find-the-pivot-integer/
class Solution:
    def pivotInteger(self, n: int) -> int:
        ll = 1
        rr = n + 1
        while rr - ll > 1:
            mm = ll + (rr - ll) // 2
            sm1 = mm * (mm + 1) // 2
            sm2 = n * (n + 1) // 2 - (mm - 1) * mm // 2
            if sm1 > sm2:
                rr = mm
            else:
                ll = mm
        sm1 = ll * (ll + 1) // 2
        sm2 = n * (n + 1) // 2 - (ll - 1) * ll // 2

        return ll if sm1 == sm2 else -1
