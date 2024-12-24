# hard
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# O(n) DP solution
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        INT_MAX = 2 ** 31 - 1

        dp = [[0, 1], [0, 0]]
        a, b = A, B
        n = len(a)
        f = 1
        nf = 1 - f
        for i in range(1, n):
            dp[f] = [INT_MAX, INT_MAX]
            if a[i] > a[i - 1] and b[i] > b[i - 1]:
                dp[f][0] = min(dp[f][0], dp[nf][0])
                dp[f][1] = min(dp[f][1], dp[nf][1] + 1)
            if a[i] > b[i - 1] and b[i] > a[i - 1]:
                dp[f][0] = min(dp[f][0], dp[nf][1])
                dp[f][1] = min(dp[f][1], dp[nf][0] + 1)
            f = 1 - f
            nf = 1 - f
        return min(dp[nf])
