# https://leetcode.com/problems/max-pair-sum-in-an-array/
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mm = {}
        for x in nums:
            d = self.maxDigit(x)
            if not d in mm:
                mm[d] = []
            mm[d].append(x)

        res = -1
        for a in mm.values():
            if len(a) == 1:
                continue
            a.sort()
            res = max(res, a[-1] + a[-2])
        return res

    def maxDigit(self, x):
        res = 0
        while x != 0:
            res = max(res, x % 10)
            x //= 10
        return res
