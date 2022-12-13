# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mm = {}
        for x in tasks:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1

        res = 0
        for x, cc in mm.items():
            if cc == 1:
                return -1
            res += (cc + 2) // 3

        return res
