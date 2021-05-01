# https://leetcode.com/problems/sum-of-digits-in-base-k/
# 1AC
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n < 0:
            return self.sumBase(-n, k)
        res = 0
        while n > 0:
            res += n % k
            n //= k
        return res
