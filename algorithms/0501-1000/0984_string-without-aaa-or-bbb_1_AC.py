# https://leetcode.com/problems/string-without-aaa-or-bbb/
# 1AC, perfect
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        def build(n1, n2, c1, c2):
            if n1 < n2:
                return build(n2, n1, c2, c1)
            res = []
            for i in range(n2):
                res.append(1)
                res.append(1)
            n1 -= n2
            if n1 > 0:
                res.append(1)
                n1 -= 1
            nr = len(res)
            for i in range(0, nr, 2):
                if n1 <= 0:
                    break
                res[i] += 1
                n1 -= 1
            for i in range(nr):
                res[i] = (c1 if i % 2 == 0 else c2) * res[i]
            return ''.join(res)

        return build(A, B, 'a', 'b')
