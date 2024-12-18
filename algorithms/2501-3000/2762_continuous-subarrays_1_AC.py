# https://leetcode.com/problems/continuous-subarrays/
# sliding window
from sortedcontainers import SortedDict

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        mm = SortedDict()
        res = 0

        n = len(nums)
        j = 0
        for i, x in enumerate(nums):
            if not x in mm:
                mm[x] = 0
            mm[x] += 1

            # check for max difference
            while True:
                cur_min = mm.iloc[0]
                cur_max = mm.iloc[-1]
                if cur_max - cur_min <= 2:
                    break

                mm[nums[j]] -= 1
                if mm[nums[j]] == 0:
                    del mm[nums[j]]
                j += 1
            res += i - j + 1

        return res
