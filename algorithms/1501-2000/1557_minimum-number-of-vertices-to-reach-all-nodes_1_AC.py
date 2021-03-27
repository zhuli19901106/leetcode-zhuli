# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
# 1AC, indegree zero
from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        mm = defaultdict(lambda: 0)
        for x, y in edges:
            mm[y] += 1
        return [x for x in range(n) if not x in mm]
