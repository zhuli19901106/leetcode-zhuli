# easy
# https://leetcode.com/problems/rings-and-rods/
# 1AC, bit ops

class Solution:
    def countPoints(self, rings: str) -> int:
        mb = {'R': 1, 'G': 2, 'B': 4}
        md = [0 for i in range(10)]
        n = len(rings) // 2
        for i in range(n):
            col, pos = rings[2 * i], ord(rings[2 * i + 1]) - ord('1')
            md[pos] |= mb[col]
        return len([x for x in md if x == 7])
