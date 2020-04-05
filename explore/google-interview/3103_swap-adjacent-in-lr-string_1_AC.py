# https://leetcode.com/problems/swap-adjacent-in-lr-string/
# 1AC
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        def convert(s):
            return [(c, i) for i, c in enumerate(s) if c != 'X']

        a_start = convert(start)
        a_end = convert(end)

        n = len(a_start)
        if len(a_end) != n:
            return False
        for i in range(n):
            if a_start[i][0] != a_end[i][0]:
                return False
            if a_start[i][0] == 'L' and a_start[i][1] < a_end[i][1]:
                return False
            if a_start[i][0] == 'R' and a_start[i][1] > a_end[i][1]:
                return False
        return True
