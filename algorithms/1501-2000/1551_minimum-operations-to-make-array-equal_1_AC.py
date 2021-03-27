# https://leetcode.com/problems/minimum-operations-to-make-array-equal/
# 1AC, a bit arithmetics
class Solution:
    def minOperations(self, n: int) -> int:
        if n & 1:
            return (n * n - 1) // 4
        else:
            return n * n // 4
