# medium
# https://leetcode.com/problems/minimum-processing-time/
# a bit tricky, sort them
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        res = 0
        n = len(processorTime)
        for i in range(n):
            res = max(res, processorTime[i] + tasks[i * 4])
        return res
