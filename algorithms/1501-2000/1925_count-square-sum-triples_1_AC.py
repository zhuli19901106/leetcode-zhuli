# easy
# https://leetcode.com/problems/count-square-sum-triples/
# 1AC

class Solution:
    def countTriples(self, n: int) -> int:
        a = [x * x for x in range(1, n + 1)]
        st = set(a)

        res = 0
        for i in range(1, n + 1):
            j = 1
            while True:
                k2 = i * i - j * j
                if k2 < j * j:
                    break
                if k2 in st:
                    res += 2
                j += 1
        return res
