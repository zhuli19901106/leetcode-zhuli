# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
# binary search
from bisect import bisect_left

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        a = sorted(arr)
        n = len(a)
        ps = [0 for i in range(n + 1)]
        ps[0] = 0
        for i in range(n):
            ps[i + 1] = ps[i] + a[i]
        if ps[n] <= target:
            return a[n - 1]

        def calcSum(val):
            i = bisect_left(a, val)
            sum_val = ps[i] + (n - i) * val
            return sum_val

        low = 0
        high = a[n - 1]
        while high - low > 1:
            mid = low + (high - low) // 2
            val = calcSum(mid)
            if val <= target:
                low = mid
            else:
                high = mid

        vl = calcSum(low)
        vh = calcSum(high)
        if vh - target < target - vl:
            return high
        else:
            return low
