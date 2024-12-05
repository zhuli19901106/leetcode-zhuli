# https://leetcode.com/problems/find-the-original-typed-string-i/
class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        res = 1
        i = 0
        while i < n:
            j = i + 1
            while j < n and word[i] == word[j]:
                j += 1
            res += j - i - 1
            i = j

        return res
