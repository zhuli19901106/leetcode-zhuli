# https://leetcode.com/problems/escape-the-ghosts/
# this problem is bugged
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        d0 = dist([0, 0], target)
        for g in ghosts:
            dg = dist(g, target)
            if dg <= d0:
                return False
        return True
