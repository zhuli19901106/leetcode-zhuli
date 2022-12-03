# https://leetcode.com/problems/best-poker-hand/
from collections import defaultdict

class Solution:
    HANDS = ['Flush', 'Three of a Kind', 'Pair', 'High Card']

    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        mr = defaultdict(lambda: 0)
        ms = defaultdict(lambda: 0)

        bh = 0

        n = len(ranks)
        for i in range(n):
            mr[ranks[i]] += 1
            ms[suits[i]] += 1
        max_s = max(ms.values())
        if max_s >= 5:
            return self.HANDS[bh]
        bh += 1

        max_r = max(mr.values())
        if max_r >= 3:
            return self.HANDS[bh]
        bh += 1

        if max_r >= 2:
            return self.HANDS[bh]
        bh += 1

        return self.HANDS[bh]
