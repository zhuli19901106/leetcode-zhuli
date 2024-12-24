# medium
# https://leetcode.com/problems/binary-trees-with-factors/
# should've been more careful
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7

        a = A
        a.sort()
        n = len(a)
        res = {}
        for i, x in enumerate(a):
            res[x] = 1
            for j in range(i):
                if a[j] > x // a[j]:
                    break
                if x % a[j] != 0 or (not x // a[j] in res):
                    continue
                mul = 2 if a[j] != (x // a[j]) else 1
                res[x] = (res[x] + mul * res[a[j]]\
                    * res[x // a[j]]) % MOD
        return sum(res.values()) % MOD
