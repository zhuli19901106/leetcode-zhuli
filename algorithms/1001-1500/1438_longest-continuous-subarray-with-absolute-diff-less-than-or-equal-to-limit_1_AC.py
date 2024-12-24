# medium
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
from sortedcontainers import SortedDict

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mm = SortedDict()
        res = 0

        n = len(nums)
        j = 0
        for i, x in enumerate(nums):
            if not x in mm:
                mm[x] = 0
            mm[x] += 1

            cur_min = mm.iloc[0]
            cur_max = mm.iloc[-1]
            if cur_max - cur_min <= limit:
                res = max(res, i - j + 1)
                continue

            while True:
                mm[nums[j]] -= 1
                if mm[nums[j]] == 0:
                    del mm[nums[j]]
                j += 1

                cur_min = mm.iloc[0]
                cur_max = mm.iloc[-1]
                if cur_max - cur_min <= limit:
                    break
            res = max(res, i - j + 1)

        return res
