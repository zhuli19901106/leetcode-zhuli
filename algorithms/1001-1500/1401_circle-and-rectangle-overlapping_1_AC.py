# medium
# https://leetcode.com/problems/circle-and-rectangle-overlapping/
# 1AC, enumerate
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        rx, ry, r = x_center, y_center, radius
        if rx >= x1 and rx <= x2:
            return ry >= y1 - r and ry <= y2 + r
        if ry >= y1 and ry <= y2:
            return rx >= x1 - r and rx <= x2 + r
        dx = x1 - rx if rx < x1 else rx - x2
        dy = y1 - ry if ry < y1 else ry - y2
        if dx **2 + dy ** 2 > r ** 2:
            return False
        return True
