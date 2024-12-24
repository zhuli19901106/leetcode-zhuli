# easy
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from bisect import bisect_left

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        res = []
        for x in nums:
            i = bisect_left(a, x)
            res.append(i)
        return res
