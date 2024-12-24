# medium
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
# O(n^3) DP with memorized search
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        INT_MAX = 2 ** 31 - 1
        n = len(A)
        dp = [[0 for j in range(n)] for i in range(n)]

        def dfs(i, j):
            nonlocal dp

            if j - i < 2:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            if j - i == 2:
                dp[i][j] = A[i] * A[i + 1] * A[i + 2]
                return dp[i][j]

            res = INT_MAX
            for k in range(i + 1, j):
                ll = dfs(i, k)
                rr = dfs(k, j)
                res = min(res, ll + A[i] * A[k] * A[j] + rr)
            dp[i][j] = res
            return res

        return dfs(0, n - 1)
