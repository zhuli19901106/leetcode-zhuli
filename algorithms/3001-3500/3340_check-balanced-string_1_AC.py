# easy
# https://leetcode.com/problems/check-balanced-string/
class Solution:
    def isBalanced(self, num: str) -> bool:
        sm0, sm1 = 0, 0
        for i, c in enumerate(num):
            if i % 2 == 0:
                sm0 += int(c)
            else:
                sm1 += int(c)
        return sm0 == sm1
