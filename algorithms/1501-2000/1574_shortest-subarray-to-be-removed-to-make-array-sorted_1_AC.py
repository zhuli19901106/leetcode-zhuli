# medium
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
# I can't think of any O(n) ways, strange
from bisect import bisect_left

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        a = arr
        n = len(a)

        i = 0
        while i < n - 1 and a[i] <= a[i + 1]:
            i += 1

        j = n - 1
        while j > 0 and a[j] >= a[j - 1]:
            j -= 1

        if j == 0:
            return 0

        # [0: i0 + 1] and [j0:] are already sorted
        i0, j0 = i, j

        res = j
        for i in range(i0 + 1):
            j = bisect_left(a, a[i], lo=j0)
            res = min(res, j - i - 1)
        return res
