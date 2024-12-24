# easy
# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        res = 0
        i = 0
        while i < n:
            if nums[i] > threshold or nums[i] % 2 == 1:
                i += 1
                continue
            j = i + 1

            while j < n and nums[j] <= threshold and (nums[j] - nums[j - 1]) % 2 == 1:
                j += 1
            res = max(res, j - i)
            i = j

        return res
