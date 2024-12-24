# medium
# https://leetcode.com/problems/four-divisors/
# product of two different primes, as well as perfect cube of a prime
# Runtime: 408 ms, faster than 100.00% of Python3 online submissions for Four Divisors.
# Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Four Divisors.
class Solution:
    def __init__(self):
        self.pf = Solution._sievePrime(50000)
        self.pfs = set(self.pf)

    def sumFourDivisors(self, nums: List[int]) -> int:
        pf = self.pf
        pfs = self.pfs

        res = 0
        for x in nums:
            i = 0
            y = None

            while pf[i] <= x // pf[i]:
                if x % pf[i] == 0:
                    y = x // pf[i]
                    break
                i += 1
            if y is None:
                continue
            if (y in pfs and y != pf[i]) or y == pf[i] ** 2:
                res += 1 + pf[i] + y + x
        return res

    @staticmethod
    def _sievePrime(n):
        ap = [True for i in range(n + 1)]
        ap[0] = ap[1] = False
        i = 2
        while i <= n // i:
            if not ap[i]:
                i += 1
                continue
            j = i
            while j <= n // i:
                ap[i * j] = False
                j += 1
            i += 1
        return [i for i, x in enumerate(ap) if x]
