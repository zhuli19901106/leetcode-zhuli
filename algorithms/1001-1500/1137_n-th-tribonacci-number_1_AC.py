# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0, 1, 1]
        if n < 3:
            return f[n]
        for i in range(3, n + 1):
            x = sum(f)
            f = [f[1], f[2], x]
        return f[2]
