# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cx, cy, cz = 0, 0, 0
        tx, ty, tz = target
        for x, y, z in triplets:
            if x > tx or y > ty or z > tz:
                continue
            cx = max(cx, x)
            cy = max(cy, y)
            cz = max(cz, z)

        return cx == tx and cy == ty and cz == tz
