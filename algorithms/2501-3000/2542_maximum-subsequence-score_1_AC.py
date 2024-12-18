# https://leetcode.com/problems/maximum-subsequence-score/
# I got the feeling that things should be sorted, but can't prove it
# should be hard, definitely
# and a really smart problem, makes me the dumb
from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a = list(zip(nums2, nums1))
        a.sort(reverse=True)

        res = 0
        cur = 0
        pq = []
        for x2, x1 in a:
            heappush(pq, x1)
            cur += x1

            if len(pq) > k:
                cur -= heappop(pq)
            if len(pq) == k:
                # because x2 is always the current min in nums2
                res = max(res, cur * x2)
        return res
