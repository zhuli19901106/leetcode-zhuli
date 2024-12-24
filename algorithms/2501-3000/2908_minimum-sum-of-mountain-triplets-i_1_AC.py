# easy
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1

        al = [0 for _ in range(n)]
        al[0] = nums[0]
        for i in range(1, n):
            al[i] = min(al[i - 1], nums[i])

        ar = [0 for _ in range(n)]
        ar[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            ar[i] = min(ar[i + 1], nums[i])

        for i in range(1, n - 1):
            if nums[i] <= al[i - 1] or nums[i] <= ar[i + 1]:
                continue
            val = al[i - 1] + nums[i] + ar[i + 1]
            if res == -1:
                res = val
            else:
                res = min(res, val)
        return res
