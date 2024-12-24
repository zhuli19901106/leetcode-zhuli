# medium
# https://leetcode.com/problems/video-stitching/
# DP, not greedy
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        a = sorted([(x, y) for x, y in clips], key=lambda p: (p[0], -p[1]))

        n = len(a)
        INT_MAX = 2 ** 31 - 1
        dp = [INT_MAX for i in range(n)]
        for i in range(n):
            if a[i][0] == 0:
                dp[i] = 1
            for j in range(i):
                if dp[j] == INT_MAX:
                    continue
                if a[j][1] < a[i][0]:
                    continue
                dp[i] = min(dp[i], dp[j] + 1)
        res = INT_MAX
        for i in range(n):
            if a[i][1] >= T and dp[i] != INT_MAX:
                res = min(res, dp[i])
        return res if res != INT_MAX else -1
