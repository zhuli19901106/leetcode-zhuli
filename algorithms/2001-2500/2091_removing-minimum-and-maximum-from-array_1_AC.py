# medium
# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_i, min_val = 0, nums[0]
        max_i, max_val = 0, nums[0]
        for i in range(1, n):
            if nums[i] < min_val:
                min_i, min_val = i, nums[i]
            if nums[i] > max_val:
                max_i, max_val = i, nums[i]

        i1, i2 = min(min_i, max_i), max(min_i, max_i)

        return min((i1 + 1) + (n - i2), n - i1, i2 + 1)
