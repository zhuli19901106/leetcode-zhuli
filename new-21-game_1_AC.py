# https://leetcode.com/problems/new-21-game/
# https://leetcode.com/problems/new-21-game/discuss/528430/C%2B%2B-solution-easy-to-understand
# markov chain, think both ways, they may be different in terms of time bound
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        n, k, w = N, K, W
        if k == 0:
            return 1.0
        if n == 0:
            return 0.0
        if n >= k + w - 1:
            return 1.0

        res = 0
        ps = 1
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = ps / w
            if i < k:
                ps += dp[i]
            else:
                res += dp[i]
            if i >= w:
                ps -= dp[i - w]
        return res
'''
# too slow
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        n, k, w = N, K, W
        if k == 0:
            return 1.0
        if n == 0:
            return 0.0

        pr = [1.0]
        ps = [0, 1.0]
        i = 0
        while i < k:
            old_len = len(pr)
            cur_len = min(len(pr), k) + w
            while len(pr) < cur_len:
                pr.append(0)
                ps.append(0)

            for j in range(i + 1, len(pr)):
                ll = max(0, j - w)
                rr = min(k - 1, j - 1, old_len - 1)
                val = (ps[rr + 1] - ps[ll]) / w
                if j >= k:
                    pr[j] += val
                else:
                    pr[j] = val

            pr[i] = 0
            ps[i + 1] = 0
            for j in range(len(ps) - 1):
                ps[j + 1] = ps[j] + pr[j]
            i += 1

        res = 0
        for i in range(k, n + 1):
            res += pr[i]
        return res
'''