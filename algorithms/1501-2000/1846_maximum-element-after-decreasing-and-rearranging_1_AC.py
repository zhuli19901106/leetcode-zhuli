# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        a = sorted(arr)
        n = len(a)
        last = 0
        for i in range(n):
            if a[i] > last + 1:
                a[i] = last + 1
            last = a[i]

        return a[n - 1]
