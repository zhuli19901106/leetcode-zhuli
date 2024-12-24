# medium
# https://leetcode.com/problems/reveal-cards-in-increasing-order/
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        a = sorted(deck)
        ia = 0
        n = len(a)
        res = [None for i in range(n)]
        q = []
        for i in range(n):
            q.append(i)
        while len(q) > 0:
            m = len(q)
            for x in q[::2]:
                res[x] = a[ia]
                ia += 1
            q = q[1::2]
            if m % 2 == 1:
                q = q[1:] + q[:1]
        return res
