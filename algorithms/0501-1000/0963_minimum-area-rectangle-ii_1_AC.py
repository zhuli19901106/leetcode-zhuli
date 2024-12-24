# medium
# https://leetcode.com/problems/minimum-area-rectangle-ii/
#brute-force and ugly
from math import sqrt

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        INT_MAX = 2 ** 31 - 1
        res = INT_MAX

        def euclid(p1, p2):
            return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])

        def isRect(sq):
            for i in range(4):
                a = []
                for j in range(4):
                    if i == j:
                        continue
                    a.append(euclid(sq[i], sq[j]))
                a.sort()
                if a[0] == 0 or a[0] + a[1] != a[2]:
                    return False, a
            return True, a

        def dfs(a, idx, sq):
            nonlocal res

            if len(sq) == 3:
                sd = sorted([euclid(sq[0], sq[1]), euclid(sq[0], sq[2]),\
                    euclid(sq[1], sq[2])])
                if sd[0] + sd[1] != sd[2]:
                    return
            if len(sq) == 4:
                ret, sd = isRect(sq)
                if ret:
                    res = min(res, sqrt(sd[0] * sd[1]))
                return
            for i in range(idx, len(a)):
                sq.append(a[i])
                dfs(a, i + 1, sq)
                sq.pop()

        dfs(points, 0, [])
        return res if res != INT_MAX else 0
