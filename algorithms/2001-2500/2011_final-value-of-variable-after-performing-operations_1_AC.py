# easy
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# 1AC

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        mm = {'++X': +1, 'X++': +1, '--X': -1, 'X--': -1}
        x = 0
        for op in operations:
            x += mm[op]
        return x
