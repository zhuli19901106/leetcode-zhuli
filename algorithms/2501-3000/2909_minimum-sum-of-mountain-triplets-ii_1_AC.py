# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1

        lm = [0 for i in range(n)]
        rm = [0 for i in range(n)]

        lm[0] = nums[0]
        for i in range(1, n):
            lm[i] = min(lm[i - 1], nums[i])
        rm[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            rm[i] = min(rm[i + 1], nums[i])

        res = -1
        for i in range(1, n - 1):
            x, y = lm[i - 1], rm[i + 1]
            if not (x < nums[i] and y < nums[i]):
                continue
            if res == -1 or res > x + nums[i] + y:
                res = x + nums[i] + y
        return res
