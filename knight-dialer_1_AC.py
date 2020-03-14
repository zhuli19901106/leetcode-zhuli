# https://leetcode.com/problems/knight-dialer/
# 1AC, simple DP
class Solution:
    def knightDialer(self, N: int) -> int:
        MOD = 10 ** 9 + 7

        g = [\
            [4, 6],\
            [6, 8],\
            [7, 9],\
            [4, 8],\
            [0, 3, 9],\
            [],\
            [0, 1, 7],\
            [2, 6],\
            [1, 3],\
            [2, 4],\
        ]
        a = [\
            [1 for i in range(10)],\
            [0 for i in range(10)],\
        ]
        f = 1
        nf = 1 - f
        for ni in range(1, N):
            for i in range(10):
                a[f][i] = 0
                for x in g[i]:
                    a[f][i] += a[nf][x]
                a[f][i] %= MOD
            f = 1 - f
            nf = 1 - f

        return sum(a[nf]) % MOD
