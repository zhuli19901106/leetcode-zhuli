# easy
# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/
# 1AC
class Solution:
    def countLetters(self, S: str) -> int:
        n = len(S)
        i = 0
        res = 0
        while i < n:
            j = i + 1
            while j < n and S[j] == S[i]:
                j += 1
            res += (j - i) * (j - i + 1) // 2
            i = j
        return res
