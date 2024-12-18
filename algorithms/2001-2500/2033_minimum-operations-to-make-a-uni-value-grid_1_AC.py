# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
# careful, it's the median, not mean
# without this prior math knowledge, it can be much harder to solve
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        min_val = 1 << 31 - 1
        for r in grid:
            min_val = min(min_val, min(r))

        a = []
        for r in grid:
            for val in r:
                if (val - min_val) % x != 0:
                    return -1
                a.append((val - min_val) // x)

        # I thought it's the mean, I was wrong
        a.sort()
        n = len(a)
        med = a[n // 2] if n % 2 == 1 else (a[n // 2 - 1] + a[n // 2]) / 2

        k = int(med)
        res1 = 0
        for val in a:
            res1 += abs(val - k)

        k += 1
        res2 = 0
        for val in a:
            res2 += abs(val - k)

        res = min(res1, res2)
        return res
