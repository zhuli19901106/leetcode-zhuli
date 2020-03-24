# https://leetcode.com/problems/closest-divisors/
from math import floor, sqrt

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def closestDiv(n):
            i = int(floor(sqrt(n)))
            while i > 1:
                if n % i == 0:
                    break
                i -= 1
            return i, n // i

        x1, y1 = closestDiv(num + 1)
        x2, y2 = closestDiv(num + 2)
        if y1 - x1 < y2 - x2:
            return [x1, y1]
        else:
            return [x2, y2]
