# medium
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
class Solution:
    def minDeletions(self, s: str) -> int:
        mm = {}
        for c in s:
            if c in mm:
                mm[c] += 1
            else:
                mm[c] = 1

        a = sorted(mm.values(), reverse=True)
        n = len(a)
        if n == 0:
            return 0

        res = 0
        cur = a[0] - 1
        for i in range(1, n):
            if a[i] >= cur:
                res += a[i] - cur
                a[i] = cur
            # watch for zero
            cur = max(0, a[i] - 1)

        return res
