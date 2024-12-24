# easy
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            if self.countOnes(i) == k:
                res += nums[i]
        return res

    def countOnes(self, x):
        res = 0
        while x != 0:
            res += (x & 1)
            x >>= 1
        return res
