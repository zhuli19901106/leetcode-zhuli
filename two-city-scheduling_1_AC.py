# https://leetcode.com/problems/two-city-scheduling/
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        class Item:
            def __init__(self, cost):
                self.cost = cost
                self.key = cost[0] - cost[1]

            def __lt__(self, other):
                return self.key < other.key

        a = sorted([Item(c) for c in costs])
        n = len(a) // 2
        res = 0
        for i in range(n):
            res += a[i].cost[0]
            res += a[i + n].cost[1]
        return res
