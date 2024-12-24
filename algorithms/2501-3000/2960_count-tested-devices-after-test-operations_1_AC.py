# easy
# https://leetcode.com/problems/count-tested-devices-after-test-operations/
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cur = 1
        res = 0
        for x in batteryPercentages:
            if x < cur:
                continue
            cur += 1
            res += 1
        return res
