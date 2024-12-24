# easy
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        max_val = [0 for i in range(n)]
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            max_val[i] = mx

        max_diff = [0 for i in range(n)]
        mx = 0
        for i in range(1, n):
            mx = max(mx, max_val[i - 1] - nums[i])
            max_diff[i] = mx

        mx = 0
        for i in range(2, n):
            mx = max(mx, max_diff[i - 1] * nums[i])
        return mx
