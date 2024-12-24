# medium
# https://leetcode.com/problems/maximize-greatness-of-an-array/
from sortedcontainers import SortedDict

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        mm = SortedDict()
        for x in nums:
            if not x in mm:
                mm[x] = 0
            mm[x] += 1

        res = 0
        for x in nums:
            i = mm.bisect_right(x)
            if i == len(mm):
                continue
            y = mm.iloc[i]
            mm[y] -= 1
            if mm[y] == 0:
                del mm[y]
            res += 1
        return res
