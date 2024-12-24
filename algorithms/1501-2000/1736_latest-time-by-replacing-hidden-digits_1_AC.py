# easy
# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/
# pointless
class Solution:
    def maximumTime(self, time: str) -> str:
        s = list(time)
        if s[0] == '?':
            if s[1] == '?':
                s[:2] = '23'
            else:
                s[0] = '2' if s[1] <= '3' else '1'
        elif s[1] == '?':
            s[1] = '3' if s[0] == '2' else '9'
        if s[3] == '?':
            s[3] = '5'
        if s[4] == '?':
            s[4] = '9'
        return ''.join(s)
