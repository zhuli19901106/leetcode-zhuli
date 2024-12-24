# easy
# https://leetcode.com/problems/maximum-units-on-a-truck/
# 1AC
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr_bt = sorted(boxTypes, key=lambda x: -x[1])
        res = 0
        cc = truckSize
        for nb, ub in arr_bt:
            if cc >= nb:
                res += nb * ub
                cc -= nb
            else:
                res += cc * ub
                break
        return res
