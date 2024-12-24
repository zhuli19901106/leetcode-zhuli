# medium
# https://leetcode.com/problems/shortest-distance-to-target-color/
# 1AC, precompute from both sides
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        ml = {}
        mr = {}
        ac = colors
        n = len(ac)
        for v in (1, 2, 3):
            ml[v] = [-1 for i in range(n)]
            mr[v] = [-1 for i in range(n)]
            ml[0] = -1
            idx = -1
            for i in range(n):
                if ac[i] == v:
                    idx = i
                ml[v][i] = idx
            idx = -1
            for i in range(n - 1, -1, -1):
                if ac[i] == v:
                    idx = i
                mr[v][i] = idx
        res = []
        for i, c in queries:
            cur = -1
            if ml[c][i] != -1:
                d = i - ml[c][i]
                if cur == -1 or cur > d:
                    cur = d
            if mr[c][i] != -1:
                d = mr[c][i] - i
                if cur == -1 or cur > d:
                    cur = d
            res.append(cur)
        return res
