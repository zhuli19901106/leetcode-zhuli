# medium
# https://leetcode.com/problems/monotone-increasing-digits/
# 1AC, precomputed
from bisect import bisect_right

class Solution:
    def __init__(self):
        LIMIT = 10 ** 9 + 1
        res = set()

        def dfs(n):
            nonlocal res
            if n > LIMIT:
                return
            res.add(n)

            d = n % 10
            n1 = n + 1
            if d < 9 and not n1 in res:
                dfs(n1)
            n1 = n * 10 + d
            if not n1 in res:
                dfs(n1)

        dfs(0)
        res = sorted(res)
        self.res = res

    def monotoneIncreasingDigits(self, N: int) -> int:
        idx = bisect_right(self.res, N) - 1
        return self.res[idx]
