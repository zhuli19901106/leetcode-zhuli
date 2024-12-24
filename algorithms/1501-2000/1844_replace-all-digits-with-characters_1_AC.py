# easy
# https://leetcode.com/problems/replace-all-digits-with-characters/
# 1AC
class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i, ch in enumerate(s):
            if i & 1:
                res.append(chr(ord(old_ch) + int(ch)))
            else:
                old_ch = ch
                res.append(ch)
        return ''.join(res)
