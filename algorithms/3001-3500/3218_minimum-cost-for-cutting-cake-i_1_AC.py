# medium
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/
# bruteforce DP, extremely error-prone
# this is a terrible interview question, almost aggressive and hostile
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        INT_MAX = (1 << 31) - 1

        mn = (m + 1) * (n + 1)
        dp = [[0 for j in range(mn)] for i in range(mn)]

        # row size
        for rl in range(1, m + 1):
            # col size
            for cl in range(1, n + 1):
                # top
                for i1 in range(m - rl + 1):
                    # left
                    for j1 in range(n - cl + 1):
                        p1 = i1 * n + j1

                        # bottom right
                        i2, j2 = i1 + rl, j1 + cl
                        p2 = i2 * n + j2

                        if rl == 1 and cl == 1:
                            continue
                        if rl == 1:
                            dp[p1][p2] = dp[p1][i2 * n + j2 - 1] + verticalCut[j2 - 2]
                            continue
                        if cl == 1:
                            dp[p1][p2] = dp[p1][(i2 - 1) * n + j2] + horizontalCut[i2 - 2]
                            continue

                        cur = INT_MAX
                        for i3 in range(i1 + 1, i2):
                            cur = min(cur, dp[p1][i3 * n + j2] + dp[i3 * n + j1][p2] + horizontalCut[i3 - 1])
                        for j3 in range(j1 + 1, j2):
                            cur = min(cur, dp[p1][i2 * n + j3] + dp[i1 * n + j3][p2] + verticalCut[j3 - 1])
                        dp[p1][p2] = cur

        # this is insane
        # for i1 in range(m):
        #     for j1 in range(n):
        #         for i2 in range(i1 + 1, m + 1):
        #             for j2 in range(j1 + 1, n + 1):
        #                 print(f'dp[{i1}][{j1}][{i2}][{j2}] = {dp[i1 * n + j1][i2 * n + j2]}')

        return dp[0][m * n + n]
