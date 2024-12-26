# hard
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
# isn't this LIS?
# why is this hard?
from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        obs = obstacles
        n = len(obs)
        if n == 0:
            return []

        a = [obs[0]]
        res = [1]
        for i in range(1, n):
            x = obs[i]
            j = bisect_right(a, x)
            res.append(j + 1)

            if j == len(a):
                a.append(x)
            else:
                a[j] = x
        return res
