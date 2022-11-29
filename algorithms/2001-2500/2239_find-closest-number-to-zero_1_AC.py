# https://leetcode.com/problems/find-closest-number-to-zero/
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_abs, min_i = abs(nums[0]), 0
        for i, x in enumerate(nums):
            if abs(x) < min_abs:
                min_abs, min_i = abs(x), i
            elif abs(x) > min_abs:
                continue
            if x > nums[min_i]:
                min_i = i

        return nums[min_i]
