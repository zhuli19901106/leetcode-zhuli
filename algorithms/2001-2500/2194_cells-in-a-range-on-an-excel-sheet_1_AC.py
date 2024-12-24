# easy
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        def parseCell(s):
            return (ord(s[0]) - ord('A'), int(s[1:]))

        def formatCell(x, y):
            return '{}{}'.format(chr(ord('A') + x), y)

        s1, s2 = s.split(':')
        x1, y1 = parseCell(s1)
        x2, y2 = parseCell(s2)
        res = []
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                res.append(formatCell(x, y))
        return res
    