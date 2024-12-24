# easy
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverseDigits(x):
            x1 = 0
            R = 10
            while x != 0:
                x1 = x1 * R + x % R
                x //= R
            return x1

        return num == reverseDigits(reverseDigits(num))
