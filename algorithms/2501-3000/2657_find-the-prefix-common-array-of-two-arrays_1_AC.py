# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sa, sb = set(), set()
        ca, cb = 0, 0

        res = []
        n = len(A)
        for i in range(n):
            if A[i] in sb:
                ca += 1
                cb += 1
            sa.add(A[i])

            if B[i] in sa:
                ca += 1
                cb += 1
            sb.add(B[i])

            res.append(min(ca, cb))
        return res
