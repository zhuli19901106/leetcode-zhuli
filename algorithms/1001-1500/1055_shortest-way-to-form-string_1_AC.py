# https://leetcode.com/problems/shortest-way-to-form-string/
# 1AC, keep scanning
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = source
        ns = len(s)
        t = target
        nt = len(t)

        i = j = 0
        res = 0
        cur = 0
        while j < nt:
            if s[i] == t[j]:
                j += 1
                cur += 1
            i += 1
            if i == ns:
                i = 0
                res += 1
                if cur == 0:
                    return -1
                else:
                    cur = 0
        if cur > 0:
            res += 1
            cur = 0
        return res
