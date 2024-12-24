# medium
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/
# just count it
class Solution:
    def maximumLength(self, s: str) -> int:
        mm = {}
        n = len(s)
        i = 0
        while i < n:
            if not s[i] in mm:
                mm[s[i]] = []

            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1

            mm[s[i]].append(j - i)
            i = j

        res = -1
        for ch, a in mm.items():
            max_cc = max(a)
            cc = [0 for i in range(max_cc)]

            for x in a:
                for i in range(x):
                    cc[i] += x - i
            for i in range(max_cc - 1, -1, -1):
                if cc[i] >= 3 and i + 1 > res:
                    res = i + 1
        return res
