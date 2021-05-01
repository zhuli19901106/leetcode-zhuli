# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
# 1AC, totally tiresome and pointless
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        at = set()
        am = set()
        tm = {}
        for _, t, m in orders:
            at.add(t)
            am.add(m)
            if not t in tm:
                tm[t] = {}
            if not m in tm[t]:
                tm[t][m] = 0
            tm[t][m] += 1

        at = [str(x) for x in sorted([int(x) for x in at])]
        am = sorted(am)
        res = []
        res.append(['Table'] + am)
        for t in at:
            row = [str(t)] + [str(x) for x in [tm[t][m] if m in tm[t] else 0 for m in am]]
            res.append(row)
        return res
