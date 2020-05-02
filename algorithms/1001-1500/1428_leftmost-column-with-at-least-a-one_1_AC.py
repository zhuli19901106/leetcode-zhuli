# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/# """
# surely it's binary search.
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        bm = binaryMatrix
        n, m = bm.dimensions()
        if n == 0 or m == 0:
            return -1

        def countOne(idx):
            res = 0
            for i in range(n):# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/# """
# surely it's binary search.
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        bm = binaryMatrix
        n, m = bm.dimensions()
        if n == 0 or m == 0:
            return -1

        def countOne(idx):
            res = 0
            for i in range(n):
                res += bm.get(i, idx)
            return res

        if countOne(0) > 0:
            return 0
        if countOne(m - 1) == 0:
            return -1
        low = 0
        high = m - 1
        while low + 1 < high:
            mid = low + (high - low) // 2
            val = countOne(mid)
            if val == 0:
                low = mid
            else:
                high = mid
        return high
