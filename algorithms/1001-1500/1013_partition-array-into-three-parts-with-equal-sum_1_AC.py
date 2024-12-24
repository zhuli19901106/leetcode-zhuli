# easy
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s0 = sum(A)
        n = len(A)
        if s0 % 3 != 0:
            return False
        s0 //= 3

        s = 0
        i = 0
        while i < n:
            s += A[i]
            i += 1
            if s == s0:
                break
        if s != s0:
            return False

        s = 0
        while i < n:
            s += A[i]
            i += 1
            if s == s0:
                break
        if s != s0:
            return False
        return True
