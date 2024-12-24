# medium
# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
# 1AC, straightforward
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for rx, ry, rr in queries:
            cnt = 0
            for x, y in points:
                if (x - rx) ** 2 + (y - ry) ** 2 <= rr ** 2:
                    cnt += 1
            res.append(cnt)
        return res
