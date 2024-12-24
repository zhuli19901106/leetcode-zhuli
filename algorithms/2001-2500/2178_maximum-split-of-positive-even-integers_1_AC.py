# medium
# https://leetcode.com/problems/maximum-split-of-positive-even-integers/

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum <= 0 or finalSum % 2 != 0:
            return []

        rt = int(finalSum ** 0.5)
        if rt * (rt + 1) > finalSum:
            rt -= 1

        remainder = finalSum - rt * (rt + 1)
        res = [2 * i for i in range(1, rt + 1)]
        res[-1] += remainder

        return res
