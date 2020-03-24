# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = 0
        for x in A:
            if x % 2 == 0:
                sum_even += x
        res = []
        for val, idx in queries:
            if A[idx] % 2 == 0:
                if val % 2 == 0:
                    sum_even += val
                else:
                    sum_even -= A[idx]
            else:
                if val % 2 == 1:
                    sum_even += A[idx] + val
            A[idx] += val
            res.append(sum_even)
        return res
