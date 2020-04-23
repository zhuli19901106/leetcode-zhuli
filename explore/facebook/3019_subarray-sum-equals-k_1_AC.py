# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3307/
# 1AC
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mm = {0: 1}
        a = nums
        n = len(a)

        res = 0
        sm = 0
        for i, x in enumerate(a):
            sm += x
            if sm - k in mm:
                res += mm[sm - k]
            mm[sm] = mm.get(sm, 0) + 1
        return res
