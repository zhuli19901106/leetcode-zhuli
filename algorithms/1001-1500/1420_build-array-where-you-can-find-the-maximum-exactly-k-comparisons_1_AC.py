# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
# the decorator @lru_cache can't be used

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        def dfs(n, m, k, mm_res):
            if (n, m, k) in mm_res:
                return mm_res[(n, m, k)]

            if n == 1:
                return 1 if k == 1 else 0

            if k <= 0:
                return 0

            cc = (m * dfs(n - 1, m, k, mm_res)) % MOD
            for i in range(1, m):
                cc = (cc + dfs(n - 1, i, k - 1, mm_res)) % MOD

            mm_res[(n, m, k)] = cc
            return cc

        res = 0
        mm_res = {}
        for i in range(1, m + 1):
            res = (res + dfs(n, i, k, mm_res)) % MOD

        return res

