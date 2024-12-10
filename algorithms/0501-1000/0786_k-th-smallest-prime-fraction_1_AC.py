# https://leetcode.com/problems/k-th-smallest-prime-fraction/
# you only need the current smallest, not everything sorted
from heapq import heappush, heappop

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        a = arr
        n = len(a)
        pq = []
        for i in range(n - 1):
            heappush(pq, (a[i] / a[n - 1], i, n - 1))

        while len(pq) > 0:
            x, i, j = heappop(pq)
            k -= 1
            if k <= 0:
                return [a[i], a[j]]
            if j - i > 1:
                heappush(pq, (a[i] / a[j - 1], i, j - 1))
        return [-1, -1]
