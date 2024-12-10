# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1, n2 = len(str1), len(str2)
        i, j = 0, 0
        while i < n1 and j < n2:
            idx1 = ord(str1[i]) - ord('a')
            idx2 = ord(str2[j]) - ord('a')
            if idx1 == idx2 or (idx1 + 1) % 26 == idx2:
                j += 1
            i += 1
        return j == n2
