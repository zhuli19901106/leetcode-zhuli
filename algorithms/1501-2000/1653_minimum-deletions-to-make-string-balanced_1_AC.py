# medium
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
# not greedy, a bit thinking

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        ra, rb = 0, 0
        for i in range(n):
            if s[i] == 'a':
                ra1 = ra
                rb1 = rb + 1
            else:
                ra1 = ra + 1
                rb1 = min(ra, rb)
            ra, rb = ra1, rb1

        return min(ra, rb)
