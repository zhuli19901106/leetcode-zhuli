# easy
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/
# how the hell is this "easy"?
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        a = nums
        n = len(a)
        inc1 = [False for i in range(n)]
        inc2 = [False for i in range(n)]

        inc1[0] = True
        for i in range(1, n):
            if a[i] <= a[i - 1]:
                break
            inc1[i] = True

        inc2[n - 1] = True
        for i in range(n - 2, -1, -1):
            if a[i] >= a[i + 1]:
                break
            inc2[i] = True

        res = 0
        for i in range(n):
            for j in range(i, n):
                left = (i == 0 or inc1[i - 1])
                right = (j == n - 1 or inc2[j + 1])
                mid = not (i > 0 and j < n - 1 and a[i - 1] >= a[j + 1])
                if left and right and mid:
                    res += 1
        return res
