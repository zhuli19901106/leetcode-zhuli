# https://leetcode.com/problems/rotated-digits/
import re

class Solution:
    def rotatedDigits(self, N: int) -> int:
        def isGood(n):
            s = f'{n}'
            if re.match('^[180]+$', s):
                return False
            if re.search('[347]', s):
                return False
            return True

        res = 0
        for i in range(1, N + 1):
            if isGood(i):
                res += 1
        return res
