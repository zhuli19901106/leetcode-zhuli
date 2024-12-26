# hard
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/
# a medium hard, two pointers
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        res = nums[k]
        min_val = nums[k]
        i, j = k - 1, k + 1
        while i >= 0 or j <= n - 1:
            pick_i = (j > n - 1 or (i >= 0 and nums[i] > nums[j]))

            if pick_i:
                min_val = min(min_val, nums[i])
                i -= 1
            else:
                min_val = min(min_val, nums[j])
                j += 1
            res = max(res, (j - i - 1) * min_val)

        return res
