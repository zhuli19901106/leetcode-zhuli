# medium
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def countChar(s):
            m = {}
            for c in s:
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
            return m

        ms = countChar(s)
        mt = countChar(t)
        res = 0
        for c in mt:
            if not c in ms:
                res += mt[c]
            elif mt[c] > ms[c]:
                res += mt[c] - ms[c]
        return res
