# medium
# https://leetcode.com/problems/remove-comments/
# https://leetcode.com/problems/remove-comments/discuss/466028/Python-very-simple-implementation-Beats-97
# my solution was similar, but not as simple
# I tried regex as well, no luck
import re

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_comment = False
        res = []
        cur = []

        for s in source:
            n = len(s)
            i = 0
            while i < n:
                ss = s[i: i + 2]
                if ss == '//' and not in_comment:
                    # normal line
                    break
                elif ss == '/*' and not in_comment:
                    # block comment now
                    in_comment = True
                    i += 1
                elif ss == '*/' and in_comment:
                    # out of block comment now
                    in_comment = False
                    i += 1
                elif not in_comment:
                    cur.append(s[i])
                i += 1

            if len(cur) > 0 and not in_comment:
                res.append(''.join(cur))
                cur = []

        return res
