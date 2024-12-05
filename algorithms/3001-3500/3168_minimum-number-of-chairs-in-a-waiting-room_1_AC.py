# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/
class Solution:
    def minimumChairs(self, s: str) -> int:
        cc = 0
        max_cc = 0
        for c in s:
            if c == 'E':
                cc += 1
                max_cc = max(max_cc, cc)
            else:
                cc -= 1
        return max_cc
