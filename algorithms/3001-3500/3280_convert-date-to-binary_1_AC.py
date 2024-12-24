# easy
# https://leetcode.com/problems/convert-date-to-binary/
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y, m, d = int(date[:4]), int(date[5:7]), int(date[8:])
        res = '{}-{}-{}'.format(self.toBinary(y), self.toBinary(m), self.toBinary(d))
        return res

    def toBinary(self, x):
        if x == 0:
            return '0'
        res = []
        while x != 0:
            res.append('1' if (x & 1) else '0')
            x >>= 1
        res.reverse()
        res = ''.join(res)

        return res
