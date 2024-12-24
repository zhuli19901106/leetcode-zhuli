# medium
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# 1AC, rather simple idea, but the index problem is driving me crazy.
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        a = A
        n = len(a)
        ps = [0 for i in range(n + 1)]
        for i in range(n):
            ps[i + 1] = ps[i] + a[i]
        
        def solve(n1, n2):
            nonlocal n, a, ps

            s1 = [0 for i in range(n + 1)]
            for i in range(n1, n + 1):
                s1[i] = max(s1[i - 1], ps[i] - ps[i - n1])
            s2 = [0 for i in range(n + 1)]
            for i in range(n, n2 - 1, -1):
                s2[i - n2] = max(s2[i - n2 + 1], ps[i] - ps[i - n2])
            res = 0
            i = n1
            while i + n2 <= n:
                res = max(res, s1[i] + s2[i])
                i += 1
            return res

        return max(solve(L, M), solve(M, L))
