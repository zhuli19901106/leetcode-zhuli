# https://leetcode.com/problems/squirrel-simulation/
# trick me more?
class Solution:
    INT_MAX = 2 ** 31 - 1

    def minDistance(self, height: int, width: int, tree: List[int],\
        squirrel: List[int], nuts: List[List[int]]) -> int:
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        min_d = Solution.INT_MAX
        res = 0
        for i, p in enumerate(nuts):
            res += 2 * dist(p, tree)
            d = dist(p, squirrel) - dist(p, tree)
            min_d = min(min_d, d)
        res += min_d
        return res
