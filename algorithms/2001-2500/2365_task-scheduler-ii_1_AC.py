# https://leetcode.com/problems/task-scheduler-ii/
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        wait = {}
        day = 0
        for x in tasks:
            if x in wait and day < wait[x]:
                day = wait[x]

            day += 1
            wait[x] = day + space
        return day
