# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# I tried greedy, but the intuition proved wrong.
# The actual idea is a more simplistic binary search with linear checking.
from bisect import bisect_left

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        a = weights
        low = max(a)
        high = sum(a)
        while high - low > 1:
            mid = low + (high - low) // 2
            nd = Solution.numDays(weights, mid)
            if nd <= D:
                high = mid
            else:
                low = mid
        if Solution.numDays(weights, low) <= D:
            return low
        else:
            return high

    @staticmethod
    def numDays(a, cap):
        cnt = 0
        s = 0
        for x in a:
            if s + x > cap:
                cnt += 1
                s = x
            else:
                s += x
        cnt += 1
        s = 0
        return cnt
