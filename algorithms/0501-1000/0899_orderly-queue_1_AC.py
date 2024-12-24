# hard
# https://leetcode.com/problems/orderly-queue/
# a total teaser, damn

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))

        res = s
        min_c = min(s)
        for i, c in enumerate(s):
            if c != min_c:
                continue
            s1 = s[i:] + s[:i]
            if s1 < res:
                res = s1

        return res
