# easy
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# 1AC
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        inv = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                inv += 1
        if inv > 1:
            return False
        elif inv == 0:
            return True
        else:
            return nums[0] >= nums[-1]
