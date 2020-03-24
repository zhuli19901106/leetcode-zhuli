# https://leetcode.com/problems/largest-perimeter-triangle/
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        a = sorted(A)
        a.reverse()
        n = len(a)
        res = 0
        for i in range(n - 2):
            if a[i] - a[i + 1] < a[i + 2]:
                res = sum(a[i: i + 3])
                break
        return res
