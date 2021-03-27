# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# 1AC, that's a joke
class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(c) for c in n])
