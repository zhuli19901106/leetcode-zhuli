# https://leetcode.com/problems/equal-row-and-column-pairs/
# hashing, but not exactly
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        R = 31

        g = grid
        n = len(g)
        ar, ac = [], []
        for i in range(n):
            h = 0
            for j in range(n):
                h = (h * R + g[i][j]) % MOD
            ar.append(h)

            h = 0
            for j in range(n):
                h = (h * R + g[j][i]) % MOD
            ac.append(h)

        res = 0
        for i in range(n):
            for j in range(n):
                if ar[i] != ac[j]:
                    continue
                k = 0
                while k < n:
                    if g[i][k] != g[k][j]:
                        break
                    k += 1
                if k == n:
                    res += 1

        return res
