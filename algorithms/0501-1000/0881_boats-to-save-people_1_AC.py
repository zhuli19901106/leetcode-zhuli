# medium
# https://leetcode.com/problems/boats-to-save-people/
# 1AC, sort and shrink from both ends
# Runtime: 468 ms, faster than 98.72% of Python3 online submissions for Boats to Save People.
# Memory Usage: 19.6 MB, less than 16.67% of Python3 online submissions for Boats to Save People.
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        a = people
        a.sort()
        n = len(a)
        res = 0
        i, j = 0, n - 1
        while i < j:
            if a[i] + a[j] <= limit:
                i += 1
            j -= 1
            res += 1
        if i == j:
            res += 1
        return res
