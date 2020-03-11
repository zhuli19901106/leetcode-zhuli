# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/class Solution:
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vs = dict([(c, 1 << i) for i, c in enumerate('aeiou')])
        m = {0: 0}
        val = 0
        res = 0
        for i, c in enumerate(s):
            if c in vs:
                val ^= vs[c]
            if val in m:
                res = max(res, (i + 1) - m[val])
            if not val in m:
                m[val] = i + 1
        return res
