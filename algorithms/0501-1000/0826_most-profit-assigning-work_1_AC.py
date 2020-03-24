# https://leetcode.com/problems/most-profit-assigning-work/
# sort and scan
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        a = list(zip(difficulty, profit))
        a.sort()
        n = len(a)
        worker.sort()

        max_val = -1
        i = 0
        res = 0
        for w in worker:
            while i < n and w >= a[i][0]:
                max_val = max(max_val, a[i][1])
                i += 1
            if max_val == -1:
                continue
            res += max_val
        return res
