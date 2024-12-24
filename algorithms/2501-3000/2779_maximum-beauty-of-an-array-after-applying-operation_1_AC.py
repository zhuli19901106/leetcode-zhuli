# medium
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/
# order doesn't matter
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0

        i = 0
        while i < n:
            res = max(res, bisect_right(nums, nums[i] + 2 * k) - i)

            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            i = j
        return res
