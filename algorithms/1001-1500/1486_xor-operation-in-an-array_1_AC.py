# https://leetcode.com/problems/xor-operation-in-an-array/
# 1AC, brute force
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= (start + 2 * i)
        return res
