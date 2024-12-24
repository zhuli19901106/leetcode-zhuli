# medium
# https://leetcode.com/problems/maximum-of-absolute-value-expression/
# that's a tricky one
# https://leetcode.com/problems/maximum-of-absolute-value-expression/discuss/480064/python3-O(n)-solution-using-basic-math-absolute-value-definition.
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        INT_MIN = -(2 ** 31)
        INT_MAX = 2 ** 31 - 1
        min_sum = [INT_MAX for i in range(4)]
        max_sum = [INT_MIN for i in range(4)]
        res = 0
        for i in range(n):
            for s1 in (-1, 1):
                for s2 in (-1, 1):
                    # expand absolute value by possibilities
                    val = s1 * arr1[i] + s2 * arr2[i] + i
                    idx = ((s1 + 1) // 2) * 2 + ((s2 + 1) // 2)
                    min_sum[idx] = min(min_sum[idx], val)
                    max_sum[idx] = max(max_sum[idx], val)
        res = max([abs(max_sum[i] - min_sum[i]) for i in range(4)])
        return res
