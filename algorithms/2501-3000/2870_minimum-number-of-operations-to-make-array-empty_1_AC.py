# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mm = {}
        for x in nums:
            if not x in mm:
                mm[x] = 1
            else:
                mm[x] += 1

        res = 0
        for x, cc in mm.items():
            if cc == 1:
                return -1
            if cc <= 3:
                res += 1
            else:
                res += (cc + 2) // 3
        return res
