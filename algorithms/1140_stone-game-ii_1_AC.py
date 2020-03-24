# https://leetcode.com/problems/stone-game-ii/
# https://leetcode.com/problems/stone-game-ii/discuss/513862/Clean-and-Short-Python-DP-%2B-Memoization
# I find this one a bit challenging
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        a = piles
        n = len(a)
        ps = [0 for i in range(n)]
        ps[-1] = a[-1]

        for i in range(n - 2, -1, -1):
            ps[i] = a[i] + ps[i + 1]

        # dp[i][j]: m = i, starting at jth pile, number of piles one can get
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[-1][i] = 0

        def search(m, j):
            nonlocal n, ps, dp

            if dp[m][j] != -1:
                return dp[m][j]
            # key here
            res = 0
            for i in range(1, min(2 * m, n - j) + 1):
                res = max(res, ps[j] - search(max(i, m), j + i))
            dp[m][j] = res
            return res

        return search(1, 0)
