# https://leetcode.com/problems/path-crossing/
# 1AC, if it's supposed to be easy, go for the easy way out
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        mm = set()
        x, y = 0, 0
        mm.add((x, y))

        offs = {'N': (0, +1), 'S': (0, -1), 'E': (+1, 0), 'W': (-1, 0)}
        cross = False
        for c in path:
            off = offs[c]
            x, y = x + off[0], y + off[1]
            if (x, y) in mm:
                cross = True
            mm.add((x, y))
        return cross
