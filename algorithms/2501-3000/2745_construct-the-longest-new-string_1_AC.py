# medium
# https://leetcode.com/problems/construct-the-longest-new-string/
# this is BS
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        res = 0

        m = min(x, y, z)
        res += 6 * m
        z -= m
        x -= m
        y -= m

        if z >= x and z >= y:
            if y != 0:
                x, y = y, x
            if x > 0:
                res += 2
                x -= 1
            if z > 0:
                res += 2 * z
                z -= z

            return res

        if x < y:
            x, y = y, x

        if z == 0:
            res += 4 * y
            if x > y:
                res += 2
                x -= 1
            x -= y
            y -= y

            return res

        if x > 0:
            res += 2
            x -= 1
        if z > 0:
            res += 2 * z
            z -= z

        return res
