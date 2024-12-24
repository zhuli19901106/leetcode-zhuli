# medium
# https://leetcode.com/problems/walking-robot-simulation/
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def sq(x, y):
            return x * x + y * y

        obs = set()
        for ob in obstacles:
            obs.add(tuple(ob))
        offs = [(0, +1), (+1, 0), (0, -1), (-1, 0)]
        nof = len(offs)
        direc = 0
        mx, my = 0, 0
        x, y = 0, 0
        for c in commands:
            if c == -2:
                direc = (direc + nof - 1) % nof
            elif c == -1:
                direc = (direc + 1) % nof
            else:
                for i in range(c):
                    x1 = x + offs[direc][0]
                    y1 = y + offs[direc][1]
                    if (x1, y1) in obs:
                        break
                    else:
                        x, y = x1, y1
                if sq(x, y) > sq(mx, my):
                    mx, my = x, y
        return sq(mx, my)
