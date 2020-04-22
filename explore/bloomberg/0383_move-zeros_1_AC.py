# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/
# 1AC
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = nums
        n = len(a)
        j = 0
        for i in range(n):
            if a[i] != 0:
                a[j] = a[i]
                j += 1
        while j < n:
            a[j] = 0
            j += 1
