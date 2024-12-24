# medium
# https://leetcode.com/problems/best-sightseeing-pair/
# O(n^2) bound, but the pruning is effectinve due to sorting.
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        INT_MIN = -(2 ** 31)
        a = sorted([(x, i) for i, x in enumerate(A)], key=lambda x: -x[0])
        res = INT_MIN
        n = len(a)
        for i in range(n - 1):
            # early stop
            if a[i][0] + a[i + 1][0] - 1 <= res:
                break
            for j in range(i + 1, n):
                # early stop
                if a[i][0] + a[j][0] - 1 <= res:
                    break
                res = max(res, a[i][0] + a[j][0] - abs(a[i][1] - a[j][1]))
        return res
