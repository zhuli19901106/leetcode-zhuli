# https://leetcode.com/problems/count-operations-to-obtain-zero/
# gcd operation

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 < num2:
            return self.countOperations(num2, num1)
        if num2 == 0:
            return 0
        return num1 // num2 + self.countOperations(num2, num1 % num2)
