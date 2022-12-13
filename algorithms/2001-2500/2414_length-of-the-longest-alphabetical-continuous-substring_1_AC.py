# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        a = [ord(c) - ord('a') for c in s]
        n = len(a)

        res = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and a[j] == a[j - 1] + 1:
                j += 1
            res = max(res, j - i)
            i = j

        return res
