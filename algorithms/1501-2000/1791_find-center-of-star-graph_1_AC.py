# easy
# https://leetcode.com/problems/find-center-of-star-graph/
# 1AC, what?
from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mm = defaultdict(lambda: 0)
        for x, y in edges:
            mm[x] += 1
            mm[y] += 1
        for k, v in mm.items():
            if v == len(edges):
                return k
        return -1
