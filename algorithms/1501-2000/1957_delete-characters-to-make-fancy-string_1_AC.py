# easy
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# 1AC

class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        res = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1

            cc = min(2, j - i)
            for _ in range(cc):
                res.append(s[i])

            i = j            
        return ''.join(res)
