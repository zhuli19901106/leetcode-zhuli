# easy
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        k -= 1
        if k < 1:
            return 0

        a = sorted(nums)
        res = a[-1] - a[0]
        n = len(a)
        for i in range(n - k):
            res = min(res, a[i + k] - a[i])
        return res
