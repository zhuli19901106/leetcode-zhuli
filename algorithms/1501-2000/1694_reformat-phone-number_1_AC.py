# easy
# https://leetcode.com/problems/reformat-phone-number/
# waste of time and tricky
import re

class Solution:
    def reformatNumber(self, number: str) -> str:
        s = re.sub('\D', '', number)
        n = len(s)
        if n < 4:
            return s

        nh = n % 3
        if nh == 1:
            nh += 3
        if nh == 0:
            s1, s2 = s, ''
        else:
            s1, s2 = s[:-nh], s[-nh:]
        if nh == 4:
            s2 = '{}-{}'.format(s2[:2], s2[2:])
        s1 = '-'.join(re.findall('\d{3}', s1))

        if s1:
            return '{}-{}'.format(s1, s2) if nh != 0 else s1
        else:
            return s2
