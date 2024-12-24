# medium
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# O(n^2) DP solution
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        a = A
        n = len(a)
        dp = [[0 for j in range(n)] for i in range(n)]
        ds = {a[0]: 0}
        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] = 2
                dt = a[j] - a[i]
                if dt in ds:
                    dp[i][j] = max(dp[i][j], dp[ds[dt]][i] + 1)
            ds[a[i]] = i

        res = 0
        for r in dp:
            res = max(res, max(r))
        return res if res > 2 else 0
