# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3300/
# 1AC
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = nums
        n = len(a)
        res = a[:]
        p = 1
        for i in range(n):
            res[i] = p
            p *= a[i]
        p = 1
        for i in range(n - 1, -1, -1):
            res[i] *= p
            p *= a[i]
        return res
