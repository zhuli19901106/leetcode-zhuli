# medium
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
# 1AC, two scans
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        a = data
        n = len(a)
        m = 0
        for x in a:
            if x == 1:
                m += 1
        i = 0
        cc = 0
        while i < m:
            if a[i] == 1:
                cc += 1
            i += 1
        res = m - cc
        while i < n:
            if a[i] == 1:
                cc += 1
            if a[i - m] == 1:
                cc -= 1
            res = min(res, m - cc)
            i += 1
        return res
