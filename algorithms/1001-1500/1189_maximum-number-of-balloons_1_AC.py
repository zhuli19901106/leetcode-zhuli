# easy
# https://leetcode.com/problems/maximum-number-of-balloons/
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def count(s):
            m = {}
            for c in s:
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
            return m

        mt = count(text)
        mb = count('balloon')
        res = len(text)
        for c in mb:
            if not c in mt:
                return 0
            else:
                res = min(res, mt[c] // mb[c])
        return res
