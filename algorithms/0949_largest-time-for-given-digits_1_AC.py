# https://leetcode.com/problems/largest-time-for-given-digits/
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        res = -1
        perms = permutations(sorted(A))
        for a in perms:
            hour = a[0] * 10 + a[1]
            minute = a[2] * 10 + a[3]
            if hour >= 24 or minute >= 60:
                continue
            res = max(res, hour * 60 + minute)
        if res != -1:
            return '{:02d}:{:02d}'.format(res // 60, res % 60)
        else:
            return ''
