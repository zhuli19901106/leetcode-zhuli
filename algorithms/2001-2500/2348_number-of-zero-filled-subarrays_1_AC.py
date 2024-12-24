# medium
# https://leetcode.com/problems/number-of-zero-filled-subarrays/
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        i = 0
        while i < n:
            if nums[i] != 0:
                i += 1
                continue
            j = i + 1
            while j < n and nums[j] == 0:
                j += 1

            res += (j - i) * (j - i + 1) // 2
            i = j

        return res
