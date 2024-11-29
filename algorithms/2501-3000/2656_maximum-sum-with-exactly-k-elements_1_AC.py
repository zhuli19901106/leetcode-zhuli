# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + k * (k - 1) // 2
