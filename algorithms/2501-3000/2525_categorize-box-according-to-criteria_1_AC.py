# https://leetcode.com/problems/categorize-box-according-to-criteria/
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        f_bulky = ((length >= 1e4 or width >= 1e4 or height >= 1e4) or \
            (length * width * height >= 1e9))
        f_heavy = (mass >= 100)

        return ('Both' if f_heavy else 'Bulky') if f_bulky \
            else ('Heavy' if f_heavy else 'Neither')
