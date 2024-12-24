# easy
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
class Solution:
    def freqAlphabets(self, s: str) -> str:
        m = {}
        for i in range(1, 10):
            m[f'{i}'] = chr(ord('a') + i - 1)
        for i in range(10, 27):
            m[f'{i}#'] = chr(ord('j') + i - 10)

        ls = len(s)
        res = []
        i = 0
        while i < ls:
            if i + 2 < ls and s[i + 2] == '#':
                res.append(m[s[i: i + 3]])
                i += 3
            else:
                res.append(m[s[i]])
                i += 1
        return ''.join(res)
