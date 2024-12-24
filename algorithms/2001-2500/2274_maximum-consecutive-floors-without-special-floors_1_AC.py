# medium
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()

        res = 0
        cur = bottom
        for x in special:
            if x < cur:
                continue
            elif x == cur:
                cur += 1
            else:
                res = max(res, x - cur)
                cur = x + 1
        if cur <= top:
            res = max(res, top - cur + 1)

        return res
