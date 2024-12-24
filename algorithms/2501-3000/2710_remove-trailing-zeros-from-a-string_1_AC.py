# easy
# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num) - 1
        while i > 0 and num[i] == '0':
            i -= 1
        return num[: i + 1]
