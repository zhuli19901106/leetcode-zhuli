# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3301/
class Solution:
    def checkValidString(self, s: str) -> bool:
        c1 = c2 = 0
        for c in s:
            if c == '(':
                c1 += 1
                c2 += 1
            elif c == ')':
                c1 -= 1
                c2 -= 1
            elif c == '*':
                c1 += 1
                c2 -= 1
            if c1 < 0:
                return False
            if c2 < 0:
                c2 = 0
        return c2 == 0
