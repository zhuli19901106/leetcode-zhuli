# https://leetcode.com/problems/longest-alternating-subarray/
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1

        i = 0
        while i < n - 1:
            diff = nums[i + 1] - nums[i]
            if diff != 1:
                i += 1
                continue

            j = i + 1
            while j < n - 1 and nums[j + 1] - nums[j] == -diff:
                j += 1
                diff = -diff
            res = max(res, j - i + 1)
            i = j

        return res
