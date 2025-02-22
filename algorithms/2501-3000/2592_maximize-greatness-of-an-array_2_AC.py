# medium
# https://leetcode.com/problems/maximize-greatness-of-an-array/
# this is much simpler

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        i, j = 1, 0
        res = 0
        while i < n:
            if nums[i] > nums[j]:
                j += 1
                res += 1
            i += 1
        return res
