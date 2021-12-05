# https://leetcode.com/problems/build-array-from-permutation/
# 1AC, permute

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            res.append(nums[nums[i]])
        return res
