# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Runtime: 76 ms, faster than 100.00% of Python3 online submissions for Find the Distance Value Between Two Arrays.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find the Distance Value Between Two Arrays.
from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        INT_MAX = 2 ** 31 - 1

        mm = {}
        for x in arr1:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        
        a = sorted(set(arr2))
        n = len(a)
        res = 0
        for k, v in mm.items():
            dd = INT_MAX
            i = bisect_left(a, k)
            if i < n:
                dd = min(dd, a[i] - k)
            if i > 0:
                dd = min(dd, k - a[i - 1])
            if dd > d:
                res += v
        return res
