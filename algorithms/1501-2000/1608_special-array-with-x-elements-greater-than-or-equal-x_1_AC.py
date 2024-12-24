# easy
# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
# I suppose this is almost medium?
from bisect import bisect_left

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        a = sorted(nums)
        n = len(a)
        if n == 0 or a[-1] < 1:
            return -1
        if a[0] >= n:
            return n
        ll, rr = 1, n
        cur_cc = 0
        while ll + 1 < rr:
            mm = ll + (rr - ll) // 2
            i = bisect_left(a, mm)
            cc = n - i
            if cc >= mm:
                ll = mm
                cur_cc = cc
            else:
                rr = mm
        return ll if ll == cur_cc else -1
