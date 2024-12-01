# https://leetcode.com/problems/semi-ordered-permutation/
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        i1, i2 = -1, -1
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                i1 = i
            elif nums[i] == n:
                i2 = i
        res = i1 + (n - 1) - i2
        if i1 > i2:
            res -= 1
        return res
