# easy
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
class Solution:
    def digitCount(self, num: str) -> bool:
        mm = {}
        a = [int(c) for c in num]
        for i in a:
            if i in mm:
                mm[i] += 1
            else:
                mm[i] = 1

        n = len(a)
        for i in range(n):
            if (not i in mm) and a[i] == 0:
                continue
            if not (i in mm and mm[i] == a[i]):
                return False
        return True
