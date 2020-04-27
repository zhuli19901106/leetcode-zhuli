# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3310/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = nums
        n = len(a)
        i = j = 0
        while i <= j and i < n:
            j = max(j, i + a[i])
            i += 1
        return j >= n - 1
