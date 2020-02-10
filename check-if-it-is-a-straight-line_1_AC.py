# https://leetcode.com/problems/check-if-it-is-a-straight-line/
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def gcd(x, y):
            if x < 0:
                return gcd(-x, y)
            if y < 0:
                return gcd(x, -y)
            while x != 0:
                x, y = y % x, x
            return y

        def normalize(x, y):
            if x == 0:
                y = 1 if y != 0 else 0
                return x, y
            if y == 0:
                x = 1 if x != 0 else 0
                return x, y
            if x < 0:
                return normalize(-x, -y)
            d = gcd(x, y)
            x //= d
            y //= d
            return x, y

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        tan0 = normalize(x1 - x0, y1 - y0)
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            tan = normalize(x - x0, y - y0)
            if tan != tan0:
                return False
        return True
