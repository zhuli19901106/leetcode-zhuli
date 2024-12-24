# medium
# https://leetcode.com/problems/valid-parenthesis-string/
# https://leetcode.com/problems/valid-parenthesis-string/discuss/543521/Java-Count-Open-Parenthesis-O(n)-time-O(1)-space-Clean-Explain
# that's really smart, I give up
class Solution:
    def checkValidString(self, s: str) -> bool:
        c1 = c2 = 0
        for ch in s:
            if ch == '(':
                c1 += 1
                c2 += 1
            elif ch == ')':
                c1 -= 1
                c2 -= 1
            elif ch == '*':
                c1 += 1
                c2 -= 1
            # not enough at best
            if c1 < 0:
                return False
            if c2 < 0:
                c2 = 0
        return c2 == 0
