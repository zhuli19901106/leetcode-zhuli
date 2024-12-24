# easy
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nneg = bisect_left(nums, 0)
        npos = len(nums) - bisect_right(nums, 0)

        return max(npos, nneg)
