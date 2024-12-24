# easy
# two liner
class Solution:
    def isHappy(self, n: int) -> bool:
        f = lambda x, y: True if x == 1 else False if x in y else f(sum([int(c) ** 2 for c in str(x)]), y | set([x]))
        return f(n, set())
