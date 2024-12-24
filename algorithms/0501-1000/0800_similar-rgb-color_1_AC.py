# easy
# https://leetcode.com/problems/similar-rgb-color/
# 1AC
class Solution:
    def similarRGB(self, color: str) -> str:
        def closest(s):
            i = int(s, 16)
            res = i // 17 * 17
            i1 = res + 17
            if i1 <= 255 and i1 - i < i - res:
                res = i1
            return '{:02x}'.format(res)

        return '#{}'.format(''.join([closest(color[i: i + 2])\
            for i in range(1, 7, 2)]))
