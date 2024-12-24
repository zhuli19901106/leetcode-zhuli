# easy
# https://leetcode.com/problems/prime-arrangements/
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        perm = [1 for i in range(n + 1)]
        for i in range(1, n + 1):
            perm[i] = perm[i - 1] * i % MOD
        
        sieve = [1 for i in range(n + 1)]
        sieve[0] = sieve[1] = 0
        for i in range(3, n + 1):
            j = 2
            while j <= i / j:
                if not sieve[j]:
                    j += 1
                    continue
                if i % j == 0:
                    sieve[i] = 0
                    break
                j += 1
        np = sum(sieve)
        return perm[np] * perm[n - np] % MOD
