# medium
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
# ridiculous
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        if n <= 1:
            return n

        ll, rr = 1, n
        while rr - ll > 1:
            mm = ll + (rr - ll) // 2
            val = mm * (mm + 1) // 2
            if val <= n:
                ll = mm
            else:
                rr = mm
        return ll
