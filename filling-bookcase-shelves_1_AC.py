# https://leetcode.com/problems/filling-bookcase-shelves/
# O(n^2) DP solution
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        b = books
        n = len(b)
        hmax = [[0 for j in range(n)] for i in range(n)]
        wsum = [0 for i in range(n + 1)]

        for i in range(n):
            wsum[i + 1] = wsum[i] + b[i][0]

        for i in range(n):
            hmax[i][i] = b[i][1]
            for j in range(i + 1, n):
                hmax[i][j] = max(hmax[i][j - 1], b[j][1])

        INT_MAX = 2 ** 31 - 1
        dp = [INT_MAX for i in range(n + 1)]
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1):
                ps = wsum[i + 1] - wsum[j]
                if ps > shelf_width:
                    continue
                dp[i + 1] = min(dp[i + 1], dp[j] + hmax[j][i])
        return dp[n]
