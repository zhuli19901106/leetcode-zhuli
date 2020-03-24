# https://leetcode.com/problems/rectangle-overlap/
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec3 = [max(rec1[0], rec2[0]), max(rec1[1], rec2[1]),\
            min(rec1[2], rec2[2]), min(rec1[3], rec2[3])]
        rec3[0] = min(rec3[0], rec3[2])
        rec3[1] = min(rec3[1], rec3[3])
        return (rec3[2] - rec3[0]) * (rec3[3] - rec3[1]) > 0
