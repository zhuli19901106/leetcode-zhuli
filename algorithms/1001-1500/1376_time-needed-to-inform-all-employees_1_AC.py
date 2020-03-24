# https://leetcode.com/problems/time-needed-to-inform-all-employees/
# max root-to-leaf path sum
# Runtime: 1388 ms, faster than 90.00% of Python3 online submissions for Time Needed to Inform All Employees.
# Memory Usage: 88.3 MB, less than 100.00% of Python3 online submissions for Time Needed to Inform All Employees.
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        path_sum = {headID: 0}

        def dfs(idx):
            nonlocal path_sum, manager

            if idx in path_sum:
                return path_sum[idx]
            par_idx = manager[idx]
            par_sum = dfs(par_idx)
            path_sum[idx] = par_sum + informTime[par_idx]
            return path_sum[idx]

        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res
