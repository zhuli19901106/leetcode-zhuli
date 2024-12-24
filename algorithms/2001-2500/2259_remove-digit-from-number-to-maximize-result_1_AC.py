# easy
# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        res_i = -1
        for i, c in enumerate(number):
            if not c == digit:
                continue
            if i < n - 1 and c < number[i + 1]:
                res_i = i
                break
            res_i = i

        return number[:res_i] + number[res_i + 1:]
