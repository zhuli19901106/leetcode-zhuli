# easy
# https://leetcode.com/problems/make-three-strings-equal/
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        n = min(n1, n2, n3)
        i = 0
        while i < n:
            if s1[i] != s2[i] or s1[i] != s3[i]:
                break
            i += 1
        return (n1 - i) + (n2 - i) + (n3 - i) if i > 0 else -1
