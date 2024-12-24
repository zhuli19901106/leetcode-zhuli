# easy
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hours = [h % 24 for h in hours]
        n = len(hours)

        mm = {}
        res = 0
        for h in hours:
            h1 = (24 - h) % 24
            if h1 in mm:
                res += mm[h1]

            if not h in mm:
                mm[h] = 1
            else:
                mm[h] += 1
        return res
