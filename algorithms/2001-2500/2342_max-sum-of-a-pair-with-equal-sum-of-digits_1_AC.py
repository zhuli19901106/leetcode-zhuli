# medium
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        a = [(self.sumDigits(x), x) for x in nums]
        a.sort()
        n = len(a)

        res = -1
        for i in range(n - 1):
            if a[i][0] == a[i + 1][0]:
                res = max(res, a[i][1] + a[i + 1][1])
        return res

    def sumDigits(self, x):
        sm = 0
        while x != 0:
            sm += x % 10
            x //= 10
        return sm
