# https://leetcode.com/problems/k-items-with-the-maximum-sum/
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        if k <= numOnes + numZeros:
            return numOnes
        return numOnes - (k - numOnes - numZeros)
