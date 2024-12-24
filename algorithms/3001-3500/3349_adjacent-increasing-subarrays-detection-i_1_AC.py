# easy
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dp[i] = dp[i + 1] + 1

        i = 0
        while i < n:
            if dp[i] >= 2 * k:
                return True
            j = i + dp[i]
            if j < n and dp[i] >= k and dp[j] >= k:
                return True
            i = j
        return False
