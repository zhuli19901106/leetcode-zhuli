# https://leetcode.com/problems/split-with-minimum-sum/description/
class Solution:
    def splitNum(self, num: int) -> int:
        digs = sorted(str(num))
        d1, d2 = [], []
        for i, d in enumerate(digs):
            if i % 2 == 0:
                d1.append(d)
            else:
                d2.append(d)
        return int(''.join(d1)) + int(''.join(d2))
