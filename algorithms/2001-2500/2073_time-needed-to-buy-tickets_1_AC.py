# easy
# https://leetcode.com/problems/time-needed-to-buy-tickets/
# 1AC, simulation

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        res = 0
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] == 0:
                    continue
                tickets[i] -= 1
                res += 1
                if tickets[k] == 0:
                    break
        return res
