# https://leetcode.com/problems/three-divisors/
# 1AC
from math import sqrt

class Solution:
    def isThree(self, n: int) -> bool:
        rt = int(sqrt(n))
        if rt ** 2 != n:
            return False
        return self.isPrime(rt)

    def isPrime(self, n):
        if n < 2:
            return False
        i = 2
        while i <= n // i:
            if n % i == 0:
                return False
            i += 1
        return True
