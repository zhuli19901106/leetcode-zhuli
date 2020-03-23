# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
# 1AC
from bisect import bisect_left, bisect_right

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        i1 = bisect_left(nums, target)
        if i1 == n or nums[i1] != target:
            return False
        i2 = bisect_right(nums, target)

        return i2 - i1 > n // 2
