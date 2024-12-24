# easy
# https://leetcode.com/problems/missing-number-in-arithmetic-progression/
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        a = arr
        n = len(a)
        d = (a[n - 1] - a[0]) // n
        if d == 0:
            return a[0]
        i = 1
        while a[i] - a[i - 1] == d:
            i += 1
        return a[i] - d
