# medium
# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # sieve it
        MAXN = 1000
        b = [True for i in range(MAXN + 1)]
        b[0] = b[1] = False
        i = 2
        while i <= MAXN // i:
            if not b[i]:
                i += 1
                continue

            j = i
            while j <= MAXN // i:
                b[i * j] = False
                j += 1
            i += 1
        ps = [i for i in range(MAXN + 1) if b[i]]

        res = set()
        for x in nums:
            res |= self.getPrimeFactors(x, ps)
        return len(res)

    def getPrimeFactors(self, x, ps):
        res = set()
        for p in ps:
            if p > x:
                break
            if x % p != 0:
                continue

            res.add(p)
            while x % p == 0:
                x //= p

        return res
