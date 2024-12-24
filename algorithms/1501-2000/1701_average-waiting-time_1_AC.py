# medium
# https://leetcode.com/problems/average-waiting-time/
# 1AC, as per request
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur = 0
        wait = 0
        for arrive, prepare in customers:
            if cur > arrive:
                wait += cur - arrive
            else:
                cur = arrive
            cur += prepare
            wait += prepare
        return wait / len(customers)
