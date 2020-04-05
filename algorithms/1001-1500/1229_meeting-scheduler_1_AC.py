# https://leetcode.com/problems/meeting-scheduler/
# 1AC, move forward and find a possible intersection
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        s1 = slots1
        s2 = slots2
        s1.sort()
        s2.sort()
        n1 = len(s1)
        n2 = len(s2)
        i1 = i2 = 0
        while i1 < n1 and i2 < n2:
            if s1[i1][1] <= s2[i2][0]:
                i1 += 1
                continue
            if s2[i2][1] <= s1[i1][0]:
                i2 += 1
                continue
            x = max(s1[i1][0], s2[i2][0])
            y = min(s1[i1][1], s2[i2][1])
            if y - x >= duration:
                return [x, x + duration]
            if s1[i1][1] < s2[i2][1]:
                i1 += 1
            else:
                i2 += 1
        return []
