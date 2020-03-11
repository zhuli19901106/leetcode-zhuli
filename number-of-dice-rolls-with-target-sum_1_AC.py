# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# DFS with memorization
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > d * f:
            return 0
        MOD = 10 ** 9 + 7
        dp = {}
        for i in range(1, f + 1):
            dp[(1, i)] = 1

        def dfs(idx, sm):
            nonlocal dp

            if (idx, sm) in dp:
                return dp[(idx, sm)]
            res = 0
            for i in range(1, f + 1):
                idx1 = idx - 1
                sm1 = sm - i
                if sm1 < idx1 or sm1 > idx1 * f:
                    continue
                res = (res + dfs(idx1, sm1)) % MOD
            dp[(idx, sm)] = res
            return res

        return dfs(d, target)
