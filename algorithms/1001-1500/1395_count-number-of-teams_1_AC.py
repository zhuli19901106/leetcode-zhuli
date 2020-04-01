# https://leetcode.com/problems/count-number-of-teams/
# 1AC, intuitive O(3 * n^2) DP
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        a = rating
        return self.lis(a) + self.lis(a[::-1])

    def lis(self, a):
        n = len(a)
        if n < 3:
            return 0
        dp = [[0 for i in range(n)] for i in range(3)]
        for i in range(n):
            dp[0][i] = 1
        for di in range(1, 3):
            for i in range(n):
                for j in range(i):
                    if a[j] >= a[i]:
                        continue
                    dp[di][i] += dp[di - 1][j]
        res = 0
        for i in range(n):
            res += dp[2][i]
        return res
