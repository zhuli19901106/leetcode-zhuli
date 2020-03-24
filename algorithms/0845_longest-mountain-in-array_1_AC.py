# https://leetcode.com/problems/longest-mountain-in-array/
# prefix and postfix counting
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        a = A
        n = len(a)
        if n < 3:
            return 0
        c1 = [0 for i in range(n)]
        c2 = [0 for i in range(n)]

        c1[0] = 1
        for i in range(1, n):
            c1[i] = c1[i - 1] + 1 if a[i] > a[i - 1] else 1

        c2[n - 1] = 1
        for i in range(n - 2, -1, -1):
            c2[i] = c2[i + 1] + 1 if a[i] > a[i + 1] else 1

        res = 0
        for i in range(1, n - 1):
            if a[i] > a[i - 1] and a[i] > a[i + 1]:
                res = max(res, c1[i - 1] + c2[i + 1] + 1)

        return res
