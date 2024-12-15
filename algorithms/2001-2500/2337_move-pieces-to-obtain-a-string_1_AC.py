# https://leetcode.com/problems/move-pieces-to-obtain-a-string/
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        a1 = [(c, i) for i, c in enumerate(start) if c == 'L' or c == 'R']
        a2 = [(c, i) for i, c in enumerate(target) if c == 'L' or c == 'R']

        n = len(a1)
        if len(a2) != n:
            return False

        for i in range(n):
            c1, i1 = a1[i]
            c2, i2 = a2[i]
            if c1 != c2:
                return False

            if c1 == 'L' and i2 > i1:
                return False

            if c1 == 'R' and i2 < i1:
                return False

        return True
