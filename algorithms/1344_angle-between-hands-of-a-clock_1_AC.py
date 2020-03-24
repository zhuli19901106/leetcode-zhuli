# https://leetcode.com/problems/angle-between-hands-of-a-clock/
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        am = 360.0 * minutes / 60
        ah = 360.0 * (hour % 12 + minutes / 60.0) / 12.0
        res = abs(am - ah)
        return min(res, 360.0 - res)
