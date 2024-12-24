# medium
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 2):
            if nums[i] == 0:
                self.flip(nums, i)
                res += 1
        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1
        return res

    def flip(self, a, i):
        if i + 2 >= len(a):
            return
        for j in range(3):
            a[i + j] = 1 - a[i + j]
