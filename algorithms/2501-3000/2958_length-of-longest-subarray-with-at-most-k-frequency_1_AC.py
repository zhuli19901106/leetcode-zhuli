# medium
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
# sliding window
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        res = 0
        mm = {}
        j = 0
        for i in range(n):
            if not nums[i] in mm:
                mm[nums[i]] = 0
            mm[nums[i]] += 1

            while mm[nums[i]] > k:
                mm[nums[j]] -= 1
                if mm[nums[j]] == 0:
                    del mm[nums[j]]
                j += 1
            res = max(res, i - j + 1)

        return res
