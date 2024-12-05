# https://leetcode.com/problems/minimum-positive-sum-subarray/
# BF
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        res = -1

        for i in range(n):
            sm = 0

            j = 0
            while j < l - 1 and i + j < n:
                sm += nums[i + j]
                j += 1
            while j < r and i + j < n:
                sm += nums[i + j]
                if sm > 0 and (res == -1 or sm < res):
                    res = sm
                j += 1
        return res
