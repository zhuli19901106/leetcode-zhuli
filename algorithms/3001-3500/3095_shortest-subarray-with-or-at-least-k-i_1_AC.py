# easy
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = -1
        for i in range(n):
            sm = 0
            for j in range(i, n):
                sm |= nums[j]
                if sm >= k:
                    res = j - i + 1 if res == -1 else min(res, j - i + 1)
        return res
