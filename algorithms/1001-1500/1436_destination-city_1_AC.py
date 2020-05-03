# https://leetcode.com/problems/destination-city/
# 1AC
from collections import defaultdict

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        deg = defaultdict(lambda: [0, 0])
        for x, y in paths:
            # out-degree
            deg[x][1] += 1
            # in-degree
            deg[y][0] += 1
        res = []
        for k, v in deg.items():
            if v[0] > 0 and v[1] == 0:
                res.append(k)
        return res[0]
