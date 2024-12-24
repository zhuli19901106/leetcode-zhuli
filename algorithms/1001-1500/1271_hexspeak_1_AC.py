# easy
# https://leetcode.com/problems/hexspeak/
import re

class Solution:
    def toHexspeak(self, num: str) -> str:
        hn = hex(int(num))[2:].upper()
        if re.search('[2-9]', hn):
            return 'ERROR'
        hn = re.sub('0', 'O', hn)
        hn = re.sub('1', 'I', hn)
        return hn
