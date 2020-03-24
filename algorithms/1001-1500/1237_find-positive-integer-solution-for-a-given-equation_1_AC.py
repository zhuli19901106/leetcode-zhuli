# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    MIN_X = 1
    MIN_Y = 1
    MAX_X = 1000
    MAX_Y = 1000
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x = Solution.MIN_X
        y = Solution.MAX_Y
        res = []
        while x <= Solution.MAX_X and y >= Solution.MIN_Y:
            val = customfunction.f(x, y)
            if val < z:
                x += 1
            elif val > z:
                y -= 1
            else:
                res.append([x, y])
                x += 1
        return res
