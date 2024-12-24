# easy
# https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        i = n - 1
        while i >= 0:
            if (ord(num[i]) - ord('0')) % 2 == 1:
                break
            i -= 1
        if i == -1:
            return ''
        return num[:i + 1]
