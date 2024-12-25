# hard
# https://leetcode.com/problems/count-all-possible-routes/
# num of city and fuel are small
# distance is huge
# this is quite an easy hard, compared to those insane graph problems
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = int(1e9 + 7)

        nl = len(locations)
        dp = [[-1 for j in range(nl)] for i in range(fuel + 1)]

        dp[fuel][start] = 1
        for f in range(fuel - 1, -1, -1):
            for i in range(nl):
                for j in range(nl):
                    if j == i:
                        continue

                    d = abs(locations[i] - locations[j])
                    if f + d > fuel or dp[f + d][j] == -1:
                        continue

                    if dp[f][i] == -1:
                        dp[f][i] = dp[f + d][j]
                    else:
                        dp[f][i] = (dp[f][i] + dp[f + d][j]) % MOD
        res = 0
        for f in range(fuel, -1, -1):
            if dp[f][finish] == -1:
                continue
            res = (res + dp[f][finish]) % MOD
        return res
