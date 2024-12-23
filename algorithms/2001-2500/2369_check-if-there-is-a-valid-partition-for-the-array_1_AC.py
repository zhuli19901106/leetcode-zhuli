# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
# not greedy, use DP
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        dp = [False for i in range(n + 1)]
        dp[0] = True
        if nums[0] == nums[1]:
            dp[2] = True

        for i in range(2, n):
            if nums[i] == nums[i - 1]:
                dp[i + 1] |= dp[i - 1]
                if nums[i] == nums[i - 2]:
                    dp[i + 1] |= dp[i - 2]

            if nums[i] == nums[i - 1] + 1 and nums[i] == nums[i - 2] + 2:
                dp[i + 1] |= dp[i - 2]
        return dp[n]
