# medium
# https://leetcode.com/problems/check-if-a-string-can-break-another-string/
# 1AC
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        n = len(s1)

        i = 0
        while i < n:
            if s1[i] < s2[i]:
                break
            i += 1
        if i == n:
            return True

        i = 0
        while i < n:
            if s1[i] > s2[i]:
                break
            i += 1
        if i == n:
            return True

        return False
