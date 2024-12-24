# medium
# https://leetcode.com/problems/adding-two-negabinary-numbers/
# 1AC, not convenient, but intuitive, thus less error-prone
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def a2n(a):
            res = 0
            for x in a:
                res = res * -2 + x
            return res

        def n2a(n):
            if n == 0:
                return [0]
            res = []
            while n != 0:
                res.append(n & 1)
                # key here
                n = -(n >> 1)
            return res[::-1]

        n1 = a2n(arr1)
        n2 = a2n(arr2)
        n3 = n1 + n2
        arr3 = n2a(n3)
        return arr3
