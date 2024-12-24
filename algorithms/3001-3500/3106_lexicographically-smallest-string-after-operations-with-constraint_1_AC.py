# medium
# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/
# this should be greedy
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        MAXC = 26

        sa = [ord(c) - ord('a') for c in s]
        ta = []
        for x in sa:
            for y in range(MAXC):
                d = min(abs(x - y), abs(MAXC - x + y))
                if k >= d:
                    k -= d
                    ta.append(y)
                    break

        i = len(ta)
        ns = len(sa)
        while i < ns:
            ta.append(sa[i])
            i += 1
        t = ''.join([chr(ord('a') + x) for x in ta])
        return t
