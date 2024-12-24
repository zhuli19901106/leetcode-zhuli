# easy
# https://leetcode.com/problems/long-pressed-name/
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def rle(s):
            res = []
            n = len(s)
            i = j = 0
            while i < n:
                if j < n and s[j] == s[i]:
                    j += 1
                else:
                    res.append((s[i], j - i))
                    i = j
            return res

        an = rle(name)
        at = rle(typed)
        if len(an) != len(at):
            return False
        n = len(an)
        for i in range(n):
            if an[i][0] != at[i][0] or an[i][1] > at[i][1]:
                return False
        return True
