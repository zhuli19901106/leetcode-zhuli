# https://leetcode.com/problems/valid-boomerang/
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
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

        p = points
        n = len(points)
        tan0 = normalize(p[1][0] - p[0][0], p[1][1] - p[0][1])
        if tan0 == (0, 0):
            return False
        for i in range(2, n):
            tan = normalize(p[i][0] - p[0][0], p[i][1] - p[0][1])
            if tan == (0, 0):
                return False
            if tan == tan0:
                return False
        return True
