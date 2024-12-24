# easy
# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        cur_t = 0
        max_i, max_t = -1, -1
        for i, t in logs:
            work_t = t - cur_t
            if max_t == -1 or max_t < work_t:
                max_i, max_t = i, work_t
            if max_t == work_t and i < max_i:
                max_i = i
            cur_t = t

        return max_i
