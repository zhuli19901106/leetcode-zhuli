# https://leetcode.com/problems/count-alternating-subarrays/
# should be easy
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] != nums[j - 1]:
                j += 1
            res += (j - i) * (j - i + 1) // 2
            i = j

        return res
