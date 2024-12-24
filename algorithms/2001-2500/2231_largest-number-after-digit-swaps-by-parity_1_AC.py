# easy
# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
class Solution:
    def largestInteger(self, num: int) -> int:
        odds, evens = [], []
        digits = list(map(int, list(str(num))))
        flags = [d % 2 for d in digits]
        for d in digits:
            if d % 2 == 0:
                evens.append(d)
            else:
                odds.append(d)

        odds.sort(reverse=True)
        evens.sort(reverse=True)
        io, ie = 0, 0
        res = []
        for f in flags:
            if f == 0:
                res.append(evens[ie])
                ie += 1
            else:
                res.append(odds[io])
                io += 1
        return int(''.join(map(str, res)))
