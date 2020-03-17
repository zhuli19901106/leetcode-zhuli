# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# supposed to be 1AC
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
        res = []

        def dfs(val, idx):
            nonlocal res

            if idx == N:
                res.append(val)
                return

            d = val % 10
            if d >= K:
                dfs(val * 10 + (d - K), idx + 1)
            if K > 0 and d + K <= 9:
                dfs(val * 10 + (d + K), idx + 1)

        for i in range(1, 10):
            dfs(i, 1)
        return res
