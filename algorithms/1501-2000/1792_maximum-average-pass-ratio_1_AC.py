# medium
# https://leetcode.com/problems/maximum-average-pass-ratio/
# this should be greedy
from heapq import heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        for x, y in classes:
            # think about it, a comparator
            heappush(pq, ((x - y) / (y * (y + 1)), x, y))

        for i in range(extraStudents):
            _, x, y = heappop(pq)
            heappush(pq, ((x - y) / ((y + 1) * (y + 2)), x + 1, y + 1))

        return sum([x / y for _, x, y in pq]) / len(pq)
