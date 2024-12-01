# https://leetcode.com/problems/total-distance-traveled/
# careful
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        mile = 0
        while mainTank >= 5:
            fill = min(mainTank // 5, additionalTank)
            mile += mainTank // 5 * 5 * 10

            mainTank = mainTank % 5 + fill
            additionalTank -= fill
        if mainTank > 0:
            mile += mainTank * 10
        return mile
