# https://leetcode.com/problems/max-chunks-to-make-sorted/
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        a = arr
        n = len(a)
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31)
        min_val = [[INT_MAX for j in range(n)] for i in range(n)]
        max_val = [[INT_MIN for j in range(n)] for i in range(n)]
        # as long as min and max values match, all in between will do
        for i in range(n):
            min_val[i][i] = max_val[i][i] = a[i]
            for j in range(i + 1, n):
                min_val[i][j] = min(min_val[i][j - 1], a[j])
                max_val[i][j] = max(max_val[i][j - 1], a[j])
        res = 0
        i = 0
        while i < n:
            j = i
            # block-wise sorted
            while j < n and not (min_val[i][j] == i and max_val[i][j] == j):
                j += 1
            i = j + 1
            res += 1
        return res
