# easy
# https://leetcode.com/problems/time-needed-to-buy-tickets/
# a bit thinking

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        xk = tickets[k]

        a = [(x, i) for i, x in enumerate(tickets)]
        a.sort()

        # for the last round, the kth person may leave early
        # but before that, every round has to be counted in full
        res = 0
        for x, i in a:
            if x >= xk and i > k:
                res -= 1

        last = 0
        cc = n
        for x, i in a:
            res += (x - last) * cc
            # early stop at last round
            if i == k:
                break

            last = x
            cc -= 1

        return res
