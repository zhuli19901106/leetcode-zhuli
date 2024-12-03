# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[0] + nums[1]

        res = 1
        for i in range(2, n - 1, 2):
            cur = nums[i] + nums[i + 1]
            if cur != last:
                break
            res += 1
        return res
