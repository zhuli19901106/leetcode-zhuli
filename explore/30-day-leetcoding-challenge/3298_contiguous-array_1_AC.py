# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3298/
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        a = nums
        n = len(a)
        mm = {0: 0}
        res = 0
        sm = 0
        for i in range(n):
            sm += 1 if a[i] == 1 else -1
            if sm in mm:
                res = max(res, i + 1 - mm[sm])
            if not sm in mm:
                mm[sm] = i + 1
        return res
