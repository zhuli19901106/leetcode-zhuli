# medium
# https://leetcode.com/problems/robot-bounded-in-circle/
# sort of a brain teaser
# Runtime: 16 ms, faster than 99.33% of Python3 online submissions for Robot Bounded In Circle.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Robot Bounded In Circle.
class Robot:
    OFFS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def __init__(self, x=0, y=0, d=0):
        self.x = x
        self.y = y
        self.d = d
    
    def move(self, z):
        self.x += z * Robot.OFFS[self.d][0]
        self.y += z * Robot.OFFS[self.d][1]
    
    def turn(self, dd):
        dd = -1 if dd < 0 else +1
        self.d = (self.d + dd) % len(Robot.OFFS)

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        r = Robot()
        for c in instructions:
            if c == 'G':
                r.move(1)
            elif c == 'L':
                r.turn(-1)
            elif c == 'R':
                r.turn(+1)
        if r.d != 0:
            return True
        return r.x == 0 and r.y == 0
