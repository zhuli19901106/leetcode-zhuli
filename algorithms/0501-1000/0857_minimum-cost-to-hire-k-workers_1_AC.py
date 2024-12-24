# hard
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/549490/Easy-Python-way-to-solve-this-O(n)-or-O(nlogn)
# hard
from heapq import heappush, heappop

class Solution:
    INT_MAX = 2 ** 31 - 1

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        # sort by max q/w ratio
        a = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
        n = len(a)
        k = K

        # max heap for q
        pq = []
        sum_q = 0
        res = Solution.INT_MAX
        for i in range(n):
            q, w = a[i]
            sum_q += q
            heappush(pq, -q)
            if len(pq) > k:
                sum_q -= -heappop(pq)
            if len(pq) == k:
                # the key is here
                res = min(res, sum_q * (w / q))
        return res
