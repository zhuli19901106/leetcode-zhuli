# medium
# https://leetcode.com/problems/longest-arithmetic-sequence/
# O(n^2) DP solution
# Runtime: 780 ms, faster than 93.17% of Python3 online submissions for Longest Arithmetic Sequence.
# Memory Usage: 145.3 MB, less than 91.67% of Python3 online submissions for Longest Arithmetic Sequence.
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        a = A
        n = len(a)
        dp = [dict() for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                dt = a[i] - a[j]
                dp[i][dt] = 2
                if dt in dp[j]:
                    dp[i][dt] = max(dp[i][dt], dp[j][dt] + 1)
        res = 0
        for i in range(1, n):
            res = max(res, max(dp[i].values()))
        return res
